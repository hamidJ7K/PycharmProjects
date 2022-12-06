import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pythonProject.pytestProject.PageObject.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.drive.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)

        self.lp.setusername("Admin")
        self.lp.setpassword("admin123")
        self.lp.clickLogin()


