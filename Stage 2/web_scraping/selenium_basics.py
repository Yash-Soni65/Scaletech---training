from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

response = driver.get("https://example.com")
element = driver.find_element(By.TAG_NAME,"h1")
print(element.text)


