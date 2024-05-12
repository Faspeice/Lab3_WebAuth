import os
import unittest
from app.crud import  add_user,check_login
from app.init import bp, db
from app.models import User

class TestCaseCrud(unittest.TestCase):
    def setUp(self):
        bp.config['TESTING'] = True
        bp.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = bp
        self.app_context = bp.app_context()
        self.app_context.push()
        db.create_all()
    def test_signup(self):
        self.assertIsNone(add_user('TestUser','TestUser@mail.ru','123456'))


    def test_add_exist_suser(self):
        self.assertIsNone(add_user('TestUser', 'TestUser@mail.ru', '123456'))
        result = add_user('TestUser', 'TestUser@mail.ru', '123456')
        self.assertIsNotNone(result, "Получил None")
        self.assertDictEqual(result,{'error': 'Такой пользователь уже существует'})


    def test_wrong_login(self):
        self.assertIsNone(add_user('TestUser', 'TestUser@mail.ru', '123456'))
        self.assertIsNone(check_login('TestUser','1234567'))
        self.assertIsNone(check_login('TestUserok', '123456'))
        self.assertIsNone(check_login('TestUser@mail.ru', '1234567'))
        self.assertIsNone(check_login('TestUser@mail.com', '123456'))
        self.assertIsNone(check_login('', ''))
    def test_correct_login(self):
        self.assertIsNone(add_user('TestUser', 'TestUser@mail.ru', '123456'))
        self.assertIsNotNone(check_login('TestUser','123456'))
        self.assertIsInstance(check_login('TestUser', '123456'),User)
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
  unittest.main()