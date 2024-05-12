import os
import unittest

from app.app import bp
from app.init import  db, app
app.register_blueprint(bp)

class AppRouteTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app
        self.client = self.app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
    def test_root(self):
        response = self.client.get('/')
        self.assertTrue('text/html' in response.content_type)

    def test_signup(self):
        response = self.client.get('/signup')
        self.assertTrue('text/html' in response.content_type)

    def test_login(self):
        response = self.client.get('/login')
        self.assertTrue('text/html' in response.content_type)

    def test_logout (self):
        response = self.client.post('/logout')
        self.assertEqual(302, response.status_code)
        self.assertTrue('/login' in response.location)
    def test_base_route_no_user(self):
        response = self.client.get('/base')
        self.assertEqual(302,response.status_code)
        self.assertTrue('/login' in response.location)

    def test_base_route_with_user(self):
        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = 'some_user_id'
            response = c.get('/base')
            self.assertEqual(response.status_code, 200)
            self.assertTrue('text/html' in response.content_type)
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
if __name__ == "__main__":
  unittest.main()