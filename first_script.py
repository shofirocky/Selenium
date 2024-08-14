from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.google.com')
#assert 'Yahoo' in browser.title
#driver.implicitly_wait(10)
elem = browser.find_element(By.ID, "input")  # Find the search box
elem.send_keys("seleniumhq")

#browser.quit()
