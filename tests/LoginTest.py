# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from tests.pages.LoginPage import LoginPage


class LoginTest(BasicTest):
  
  def setUp(self):
    super(LoginTest, self).setUp()
    self.auth()
    
  def test_login(self):
    self.login_page.sign_in(self.login, self.password)
    
#   def test_wrong_password(self):
#     wrong_password = 'wrongpassword'
#     self.login_page.sign_in(self.login, wrong_password)
#     test_validation = self.login_page.get_validation_message()
#     expected_validation1 = 'Неверный пароль, попробуйте ещё раз'
#     expected_validation2 = 'Incorrect password. Try again'
#     self.assertIn(test_validation, [expected_validation1, expected_validation2])
    
#   def test_yandex_login(self):
#     test_login = '123@yandex.ru'
#     self.login_page.enter_login(test_login)
#     self.login_page.click_continue()
#     self.login_page.wait_redirect('https://passport.yandex.ru/auth')
  