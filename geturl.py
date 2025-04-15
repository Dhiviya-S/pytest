import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print("Title of the webpage:",driver.title)
print("Current URL of the webpage:", driver.current_url)
with open("Webpage_task_11.txt","w") as file:
    file.write(driver.page_source)
time.sleep(5)  # Wait for results to load
driver.quit()
