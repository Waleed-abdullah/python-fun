from selenium import webdriver
from selenium.webdriver.common.by import By

chromeBrowser = webdriver.Chrome('./chromedriver')

chromeBrowser.maximize_window()
chromeBrowser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

showMessageButton = chromeBrowser.find_element(By.CLASS_NAME,'btn-default')
print(showMessageButton.get_attribute('innerHTML'))

assert 'Show Message' in chromeBrowser.page_source

userMessage = chromeBrowser.find_element(By.ID, 'user-message')
userMessage.clear()
userMessage.send_keys('I am extra cool')

showMessageButton.click()

chromeBrowser.quit()