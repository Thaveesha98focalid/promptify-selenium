from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # search what happen in there
time.sleep(1)

# check_Box = driver.find_element(By.CSS_SELECTOR, "#RESULT_CheckBox-8_0")
# check_Box.send_keys(Keys.SPACE)

check_Boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")  # search how to generate x path like this

for checkbox in check_Boxes:
    checkbox.send_keys(Keys.SPACE)

check_Box_count = 0

for checkbox in check_Boxes:
    if checkbox.is_selected():
        check_Box_count += 1

expected_checkbox_count = 7

if check_Box_count == expected_checkbox_count:
    print('checkbox count verified')
else:
    print('checkbox count mismatch')
