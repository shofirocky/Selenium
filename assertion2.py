from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
Expected_title = "Swag Labs"
  
# Navigating to the GeeksforGeeks website 
driver.get("https://www.saucedemo.com/") 
  
# Retrieving the actual title of the web page 
Actual_title = driver.title 
  
# Checking if the actual title is equal to the expected title 
if Actual_title == Expected_title: 
    # Assertion to indicate that the titles match 
    assert True
  
# Closing the WebDriver 
driver.close() 