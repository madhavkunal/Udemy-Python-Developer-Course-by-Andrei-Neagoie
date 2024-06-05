from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# Locate the element directly without waiting
button_element = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
print(button_element)

# Perform actions on the button_element if needed

# Keep the browser open until manually closed
print("The browser will remain open until you close it manually.")
while True:
    pass

# chrome_browser.quit()