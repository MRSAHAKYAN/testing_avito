from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ..BaseUrls import BaseUrls

class BasicPage(BaseUrls):

    driver = None

    def __init__(self, driver):
      self.driver = driver

    def wait_redirect(self, url, timeout=100):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_render(self, selector, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_render_by_name(self, name, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.NAME, name)))