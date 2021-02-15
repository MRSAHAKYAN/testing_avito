from BasicPage import BasicPage

class ThingsPage(BasicPage):
  first_thing = "a[data-marker='item-title']:first-of-type"
  # buy_btn = "button[data-marker='delivery-item-button-main']"
  buy_btn = "a[data-marker='item-title']:first-of-type"

  
  def open(self):
    self.driver.get(self.THINGS_URL)
    
  def click_first_thing(self):
    elem = self.wait_render(self.first_thing)
    elem.click()
    
  def switch_tab_to_last(self):
    self.driver.window_handles[-1]
    
  def click_buy_btn(self):
    elem = self.wait_render(self.buy_btn)
    elem.click()
    
