# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.maximize_window()
#
# username = "standard_user"
# password = "secret_sauce"
#
# login_url = "https://www.saucedemo.com/v1/"
# driver.get(login_url)
#
# username_field = driver.find_element(By.ID, "user-name")
# password_field = driver.find_element(By.ID, "password")
#
# username_field.send_keys(username)
# password_field.send_keys(password)
#
# login_button = driver.find_element(By.ID, "login-button")
# login_button.click()
#
# success_element = driver.find_element(By.CSS_SELECTOR, "product_label")
# assert success_element.text == "Products"
# from telnetlib import EC


# promptify example
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Firefox()
# driver.maximize_window()
#
# username = "thaveesha@datafab.ai"
# password = "thaveesha@123"
#
# login_url = "http://localhost:3000"
# driver.get(login_url)
#
# wait = WebDriverWait(driver, 10)

# # Wait for username field to be present
# username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
# username_field.send_keys(username)
#
# # Wait for password field to be present
# password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
# password_field.send_keys(password)
#
# # Wait for login button to be clickable
# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/button")))
# login_button.click()
#
# # Wait for the success element to be visible
# success_element = wait.until(
#    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-nowrap')
#    and contains(text(), 'Prompt')]/p[contains(text(), 'Leverage the power of LLM')]"))
# )
#
# # Assert that the success message is correct
# assert success_element.is_displayed(), "Success element is not displayed"
# assert success_element.text == "Leverage the power of LLM", "Success message text is incorrect"
#
#
# # Optionally print the text to verify
# print("Success message:", success_element.text)
#
# # Close the browser
# # driver.quit()


# promptify example normal sleep method
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.maximize_window()

username = "thaveesha@datafab.ai"
password = "thaveesha@123"

login_url = "http://localhost:3000"
driver.get(login_url)

wait = WebDriverWait(driver, 30)

try:
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    username_field.send_keys(username)

    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/button")))
    login_button.click()

    success_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[1]/div[2]")))

    assert "Prompt" in success_element.text

    chat_command_01 = "I need to run KYC on adidas domiciled in germany"
    chat_command_04 = "I want you to build a screening bag for all entities related to adidas"
    chat_command_05 = "What templates are there in the system right now?"
    chat_command_06 = "Now show me which watch lists are maintained in system"

    chat_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/div/input")))
    chat_input.send_keys(chat_command_01)
    chat_input.send_keys(Keys.RETURN)

    entity_search = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".fill-primary-green-blue-3")))
    droppable_area = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".react-grid-layout")))

    actions = ActionChains(driver)
    actions.drag_and_drop(entity_search, droppable_area).perform()

    more_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, r".\!bg-transparent > div:nth-child(1) > "
                                                     r"div:nth-child(1) > div:nth-child(2) > button:nth-child(1)")))
    more_button.click()

    time.sleep(2)

    full_view = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.text-nowrap:nth-child(2) > span:nth-child(2)")))

    full_view.click()

    time.sleep(1)

    action_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".max-h-fit > div:nth-child(1) > table:nth-child(1) >"
                                                     " tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) >"
                                                     " div:nth-child(1) > svg:nth-child(1)")))
    action_button.click()

    Adidas_Entity_profile = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.text-nowrap:nth-child(1)")))

    # Uncomment for debugging purposes
    # print("Adidas Entity Profile Text:", Adidas_Entity_profile.text)

    # assert "Adidas" in Adidas_Entity_profile.text

    chat_input.send_keys(chat_command_04)
    chat_input.send_keys(Keys.RETURN)

    Screening_widget = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#widget_4 > div:nth-child(2) > "
                                                         "div:nth-child(1) > div:nth-child(2)")))

    chat_input.send_keys(chat_command_05)
    chat_input.send_keys(Keys.RETURN)

    Template_management_widget = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#widget_6 > div:nth-child(2) >"
                                                         " div:nth-child(1) > div:nth-child(2)")))

    chat_input.send_keys(chat_command_06)
    chat_input.send_keys(Keys.RETURN)


except Exception as error:
    print("An error occurred:", error)

finally:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    time.sleep(5)
    # driver.quit()
