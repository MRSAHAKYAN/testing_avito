from BasicPage import BasicPage
import time

class ThingsPage(BasicPage):
  first_thing = "a[data-marker='item-title']:first-of-type"
  buy_btn = "button[data-marker='delivery-item-button-main']"
  phone_field_name = 'phone'
  
  login_input = 'login'
  password_input = 'password'
  submit_btn = 'submit'

  def open(self):
    self.driver.get(self.THINGS_URL)
    
  def click_first_thing(self):
    elem = self.wait_render(self.first_thing)
    elem.click()
    
  def switch_tab_to_last(self):
    last_tab = self.driver.window_handles[-1]
    self.driver.switch_to_window(last_tab)
    
  def click_buy_btn(self):
    elem = self.wait_render(self.buy_btn)
    elem.click()
    
  def enter_phone_field(self, phone):
    phone_field = self.wait_render_by_name(self.phone_field_name)
    phone_field.send_keys(phone)
    
  def get_phone_field_value(self):
    phone_field = self.wait_render_by_name(self.phone_field_name)
    return phone_field.get_attribute('value')
  
  def enter_login(self, login):
    elem = self.wait_render_by_name(self.login_input)
    elem.send_keys(login)
    
  def enter_password(self, password):
    elem = self.wait_render_by_name(self.password_input)
    elem.send_keys(password)
    
  def click_submit_btn(self):
    elem = self.wait_render_by_name(self.submit_btn)
    elem.click()

  def sign_in(self, login, password):
    self.enter_login(login)
    self.enter_password(password)
    self.click_submit_btn()