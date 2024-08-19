from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.NAME, "user-name") 
username_input.send_keys("standard_user") 
password_input = driver.find_element(By.NAME, "password")   
password_input.send_keys("secret_sauce")  
login_button = driver.find_element(By.NAME, "login-button") 
login_button.click()

driver.close()
