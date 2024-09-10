import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)
driver.maximize_window()
# driver.fullscreen_window()
# driver.minimize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(5)
driver.close()
