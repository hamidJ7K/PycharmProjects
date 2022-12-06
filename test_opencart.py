import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serviceObject = Service('/pythonProject/RobotFramework/Selenuim/chromedriver.exe')
# driver = webdriver.Chrome(service = serviceObject)
# driver.implicitly_wait(10)
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')
driver.maximize_window()


# MyWait = WebdriverWait(driver, 20)

# driver.find_element(By.XPATH, '//span[normalize-space()='My Account']').click()
# driver.find_element(By.XPATH, '//a[normalize-space()='Register']').click()
driver.find_element(By.ID, 'input-firstname').send_keys('totoName3')
driver.find_element(By.ID, 'input-lastname').send_keys('totoLastName3')
driver.find_element(By.ID, 'input-email').send_keys('totoNameDemo20223@gmail.com')
driver.find_element(By.ID, 'input-password').send_keys('totoPass2022+3')
time.sleep(4)

driver.find_element(By.CSS_SELECTOR, '#input-newsletter-yes').click()
time.sleep(4)
driver.find_element(By.NAME, 'agree').click()


time.sleep(4)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()




time.sleep(4)
driver.close()

