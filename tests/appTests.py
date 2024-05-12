import os
import unittest


from app.init import bp, db


class AppRouteTestCase(unittest.TestCase):
    def setUp(self):
        bp.config['TESTING'] = True
        bp.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = bp
        self.client = self.app.test_client()
        self.app_context = bp.app_context()
        self.app_context.push()
        db.create_all()

    def test_base_route_no_user(self):
        response = self.client.get('/')
        self.assertEqual(302,response.status_code)
        self.assertTrue('/login' in response.location)
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
  unittest.main()