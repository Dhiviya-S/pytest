import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print("Title of the webpage:",driver.title)
actual_title=driver.title
print("Current URL of the webpage:", driver.current_url)
actual_url=driver.current_url
with open("Webpage_task_11.txt","w") as file:
    file.write(driver.page_source)

@pytest.fixture
def title():
    return actual_title

def test_title_positive(title):
    assert actual_title == "Swag Labs"

def test_title_negative(title):
    assert actual_title =="Sauce Lab"

@pytest.fixture
def url():
    return actual_url

def test_positive_url(url):
    assert actual_url == "https://www.saucedemo.com/"

def test_negative_url(url):
    assert actual_url =="https://www.swagdemo.com/"


driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)  # Wait for the page to load

login_button=driver.find_element(By.ID, "login-button").click()
print("URL after login credentials:",driver.current_url)
loginn_url=driver.current_url

@pytest.fixture
def login_url():
    return loginn_url

def test_positive_loginurl(login_url):
    assert loginn_url == "https://www.saucedemo.com/inventory.html"

def test_negative_loginurl(login_url):
    assert loginn_url =="https://www.saucedemo.com/payment.html"


time.sleep(5)
driver.quit()