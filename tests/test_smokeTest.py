# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    # self.driver = webdriver.Firefox()
    # self.vars = {}   
      options = Options()
      options.add_argument("--headless=new")
      self.driver = webdriver.Firefox(options=options)
      self.vars = {}
      
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Osagie")
    self.driver.find_element(By.NAME, "lname").click()
    self.driver.find_element(By.NAME, "lname").send_keys("Ohenhen")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Blue Edge")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Systems Analyst")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("wrongUsername")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("wrongpassword")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9)").text.strip() == "Teton Turf and Tree\n4735 East Hwy 33\nSugar City, ID 83448\nWebsite"
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1191, 692)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
  
