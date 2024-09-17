from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if username and password and submit is not None:
    print('Элементы найдены')
else:
    print('Элемент не найден')