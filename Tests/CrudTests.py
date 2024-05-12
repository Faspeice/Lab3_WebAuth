import os
import unittest
from app.crud import  add_user,check_login
from app.init import app, db


class TestCrud(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
    def test_add_user(self):
        self.assertIsNone(add_user('TestUser','TestUser@mail.ru','123456'))

    def test_add_exist_suser(self):
        self.assertIsNone(add_user('TestUser', 'TestUser@mail.ru', '123456'))
        result = add_user('TestUser', 'TestUser@mail.ru', '123456')
        self.assertIsNotNone(result, "Получил None")
        self.assertDictEqual(result,{'error': 'Такой пользователь уже существует'})

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
  unittest.main()