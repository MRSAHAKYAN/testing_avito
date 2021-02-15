# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage


class BasicTest(unittest.TestCase):
    
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')
    
    def setUp(self):
        self.driver = webdriver.Chrome(config.DRIVER)
            
    def tearDown(self):
        self.driver.quit()

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.sign_in(self.login, self.password)