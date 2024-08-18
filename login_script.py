from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.NAME, "username") 
username_input.send_keys("your_username") 
password_input = driver.find_element(By.NAME, "password")   
password_input.send_keys("your_password")  
login_button = driver.find_element(By.XPATH, "//button[@type='submit']") 
login_button.click()

driver.close()