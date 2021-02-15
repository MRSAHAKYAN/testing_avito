# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from tests.pages.ThingsPage import ThingsPage


class ThingsTest(BasicTest):
  def setUp(self):
    super(ThingsTest, self).setUp()
    self.things_page = ThingsPage(self.driver)
        
  def test_empty_number(self):
    self.things_page.open()
  
    self.things_page.click_first_thing()
    self.things_page.switch_tab_to_last()
    self.things_page.click_buy_btn() 
    
    self.things_page.sign_in(self.login, self.password)
    phone = self.things_page.get_phone_field_value()
    self.assertEqual(0, len(phone))
    
    