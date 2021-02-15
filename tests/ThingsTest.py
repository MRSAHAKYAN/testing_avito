# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from tests.pages.ThingsPage import ThingsPage


class ThingsTest(BasicTest):
  def setUp(self):
    super(ThingsTest, self).setUp()
    self.things_page = ThingsPage(self.driver)
    self.auth()
        
  def test_empty_number(self):
    self.things_page.open()
  
    self.things_page.click_first_thing()
    self.things_page.switch_tab_to_last()
    self.things_page.click_buy_btn() 
    # login_field.get_attribute('value')
    
    