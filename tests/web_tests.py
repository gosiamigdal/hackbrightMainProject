from flask.ext.testing import TestCase
import web

class WebAppTest(TestCase):

    def create_app(self):
        web.app.config['TESTING'] = True
        return web.app

    def test_plan_create_message(self):
        response = self.client.get("/")
        self.assertIn('Create a new plan', response.data)

