from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver.implicitly_wait(20)
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.NAME, "user-name") 
username_input.send_keys("standard_user") 
password_input = driver.find_element(By.NAME, "password")   
password_input.send_keys("secret_sauce")  
time.sleep(10)
login_button = driver.find_element(By.NAME, "login-button") 
login_button.click()
time.sleep(10)
assert "Swag La" in driver.title

driver.close()
