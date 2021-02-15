from BasicPage import BasicPage


class LoginPage(BasicPage):
  login_input = 'login'
  password_input = 'password'
  submit_btn = 'submit'
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
    
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