import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Regle 1 Nom de fichier devrait commnecer par le mot "test"
# Regle #2 Nom des methodes devrait commencer par le mot "test"

# def setup_module(module):
#     print("Ouverture la connexion BD")
#
# def teardown_module(module):
#     print("Cloture la connexion BD")
#
#
# #def setup_function(fonction):
#     print("Ouverture du site loginsalseforce")
#
#
# def teardown_function(function):
#   print("Fermeture du navigateur")
from webdriver_manager.chrome import ChromeDriverManager


def get_data():
    return [
        ("hamid","123456"),
        ("hamid1", "123456A"),
        ("hamid2", "123456B"),
        ("hamid3", "123456C"),
        ("Admin", "admin123"),
    ]

def setup_function():
    global driver
    # serviceObject = Service('C:\\Users\\User\\PycharmProjects\\pythonProject\\RobotFramework\\Selenuim\\chromedriver.exe')
    # driver = webdriver.Chrome(service=serviceObject)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def teardown_function():
    time.sleep(4)
    driver.close()

@pytest.mark.parametrize("username, password",get_data())
def test_login(username, password):
    #print(username, "----", password,"----")

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()

def test_registreAccount():
    # driver.find_element(By.XPATH, '//span[normalize-space()='My Account']').click()
    # driver.find_element(By.XPATH, '//a[normalize-space()='Register']').click()
    driver.find_element(By.ID, 'input-firstname').send_keys('totoName2')
    driver.find_element(By.ID, 'input-lastname').send_keys('totoLastName2')
    driver.find_element(By.ID, 'input-email').send_keys('totoNameDemo20222@gmail.com')
    driver.find_element(By.ID, 'input-password').send_keys('totoPass2022+2')
    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, '#input-newsletter-yes').click()
    time.sleep(4)
    driver.find_element(By.NAME, 'agree').click()

    time.sleep(4)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()





