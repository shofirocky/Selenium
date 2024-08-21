from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
#driver.implicitly_wait(20)
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.NAME, "user-name") 
username_input.send_keys("standard_user") 
password_input = driver.find_element(By.NAME, "password")   
password_input.send_keys("secret_sauce") 
wait=WebDriverWait(driver,10) 
wait.until(EC.element_to_be_clickable((By.NAME,"login-button"))).click()
#login_button = driver.find_element(By.NAME, "login-button") 
#login_button.click()
#time.sleep(10)
assert "Swag La" in driver.title
driver.close()

