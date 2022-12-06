from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


def setup_function():
    global driver
    # serviceObject = Service('C:\\MyProject\\Selenium\\chromedriver.exe')
    # driver = webdriver.Chrome(service=serviceObject)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


def teardown_funtion():
    time.sleep(10)
    driver.quit()

def test_register():
    driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')
    driver.maximize_window()
    # driver.implicitly_wait(10)
    # MyWait = WebDriverWait(driver, 20)
    driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys('TestFName1')
    driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('TestLName1')
    driver.find_element(By.XPATH,'//input[@name="email"]').send_keys('testemail1@gmail.com')
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('P@ssw0rd1')
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, '#input-newsletter-yes').click()
    # MyRadio = MyWait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#input-newsletter-yes')))
    # MyRadio.click()
    time.sleep(4)
    driver.find_element(By.NAME,'agree').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()