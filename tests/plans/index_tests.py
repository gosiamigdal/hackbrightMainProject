from flask.ext.testing import TestCase
from app import app, db
from datetime import datetime
from app.plans.models import Plan

class PlansIndexTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_plan_create_message(self):
        response = self.client.get("/plans/")
        self.assertIn('Create a new plan', response.data)

    def test_plan_display(self):
        plan = Plan('I apparently do not like loud music at 11pm', datetime.utcnow(), datetime.utcnow())
        db.session.add(plan)
        db.session.commit()

        response = self.client.get("/plans/")
        self.assertIn("I apparently do not like loud music at 11pm", response.data)
