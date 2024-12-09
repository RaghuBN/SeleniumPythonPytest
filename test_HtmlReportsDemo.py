from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestHollandBarret:

   @pytest.fixture()
   def setup(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       yield
       self.driver.close()

   def test_homePageTitle(self,setup):
       self.driver.get("https://auth.hollandandbarrett.com/u/login")
       assert self.driver.title == "Sign in - to your account, for the best experience"

   def test_login(self,setup):
       self.driver.get("https://auth.hollandandbarrett.com/u/login")
       self.driver.find_element(By.ID, 'username').send_keys("raghu.astepahead@gmail.com")
       self.driver.find_element(By.ID, "password").send_keys("raghuBN@123")
       self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
       assert self.driver.title