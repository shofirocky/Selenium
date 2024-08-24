from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


Expected_title = "GeeksforGeeks | A computer science portal for geek"
  
# Navigate to the GeeksforGeeks website 
driver.get("https://www.geeksforgeeks.org/") 
  
# Retrieve the actual title of the web page 
Actual_title = driver.title 
  
# Assert that the actual title is equal to the expected title 
assert Actual_title == Expected_title, "Title mismatch"
  
# Close the WebDriver 
driver.close() 