from flask.ext.testing import TestCase
from app import app, db
from app.plans.models import Plan
from datetime import datetime, timedelta

class ModelsTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    CURRENT_TIME = datetime.utcnow()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def create_plan(self, name='driving a dinner plate'):
        now = ModelsTest.CURRENT_TIME
        later = ModelsTest.CURRENT_TIME + timedelta(seconds=2)

        plan = Plan(name, now, later)
        db.session.add(plan)
        db.session.commit()

        return Plan.query.all()[-1]

    def test_plan_creation(self):
        plan = self.create_plan()
        self.assertIn(plan, db.session)

    def test_plan_name_assignment(self):
        plan = self.create_plan()
        self.assertEqual(plan.name, 'driving a dinner plate')

        plan = self.create_plan('tacos for breakfast')
        self.assertEqual(plan.name, 'tacos for breakfast')

    def test_plan_start_date(self):
        plan = self.create_plan()
        self.assertEqual(plan.start_date, ModelsTest.CURRENT_TIME)

    def test_plan_end_date(self):
        plan = self.create_plan()
        self.assertEqual(plan.end_date, ModelsTest.CURRENT_TIME + timedelta(seconds=2))
