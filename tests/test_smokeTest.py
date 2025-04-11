import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class TestSmokeTest:
    def setup_method(self):
        options = Options()
        options.add_argument("--headless=new")
        service = Service(executable_path=r'C:\WebDriver\bin\geckodriver.exe')
        self.driver = webdriver.Firefox(options=options, service=service)
        self.driver.implicitly_wait(10)  # Implicit wait for all elements

    def teardown_method(self):
        self.driver.quit()

    def open_homepage(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1191, 692)

    def test_home_page(self):
        self.open_homepage()
        self.driver.find_element(By.LINK_TEXT, "Home").click()

        assert self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
        assert self.driver.title == "Teton Idaho CoC"

        self.driver.find_element(By.LINK_TEXT, "Home").click()
        assert self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
        assert self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
        assert self.driver.find_elements(By.LINK_TEXT, "Join Us!")

        self.driver.find_element(By.LINK_TEXT, "Join Us!").click()

    def test_admin_page_invalid_login(self):
        self.open_homepage()
        self.driver.find_element(By.LINK_TEXT, "Admin").click()

        self.driver.find_element(By.ID, "username").send_keys("wrongUsername")
        self.driver.find_element(By.ID, "password").send_keys("wrongpassword")
        self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".errorMessage"),
                "Invalid username and password."
            )
        )

    def test_directory_page(self):
        self.open_homepage()
        self.driver.find_element(By.LINK_TEXT, "Directory").click()

        self.driver.find_element(By.ID, "directory-grid").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"

        self.driver.find_element(By.ID, "directory-list").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"

    def test_join_page_submission(self):
        self.open_homepage()
        self.driver.find_element(By.LINK_TEXT, "Join Us").click()

        self.driver.find_element(By.NAME, "fname").send_keys("Osagie")
        self.driver.find_element(By.NAME, "lname").send_keys("Ohenhen")
        self.driver.find_element(By.NAME, "bizname").send_keys("Blue Edge")
        self.driver.find_element(By.NAME, "biztitle").send_keys("Systems Analyst")
        self.driver.find_element(By.NAME, "submit").click()

        assert self.driver.find_elements(By.NAME, "email")
