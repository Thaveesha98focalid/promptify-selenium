import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element(driver, locator, timeout=10, max_wait_time=120):
    start_time = time.time()  # Record the start time
    while True:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_wait_time:
                print(f"Element {locator} not found after {max_wait_time / 60} minutes.")
                raise Exception("Stopping process due to timeout")
            print(f"Element {locator} not found. Retrying...")


driver = webdriver.Chrome()
driver.maximize_window()

username = "thaveesha@datafab.ai"
password = "thaveesha@123"

login_url = "https://promptify.datafabdevelopment.com/"
driver.get(login_url)

try:
    # Wait for the username field and login process
    username_field = wait_for_element(driver, (By.XPATH, "//input[@type='text']"), max_wait_time=120)
    username_field.send_keys(username)

    password_field = wait_for_element(driver, (By.XPATH, "//input[@type='password']"), max_wait_time=120)
    password_field.send_keys(password)

    login_button = wait_for_element(driver, (By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/button"), max_wait_time=120)
    login_button.click()

    # Wait for elements and execute commands (with 2-minute timeouts)
    success_element = wait_for_element(driver, (By.CSS_SELECTOR,
                                                r"body > div.h-full.w-1\/4.min-w-\[304px\] > div > div > "
                                                r"div.extend-beyond-borders.w-full.p-0 > div > "
                                                r"div.flex.w-full.flex-row.items-center.justify-start > "
                                                r"div.text-nowrap.bg-transparent.p-\[5px\].px-\["
                                                r"8px\].text-sm.font-medium.text-green-blue-2"),
                                       max_wait_time=120)

    chat_input = wait_for_element(driver, (By.CSS_SELECTOR,
                                           r"body > div.h-full.w-1\/4.min-w-\[304px\] > div > div > "
                                           r"div.flex-2.overflow-y-auto.p-2 > div > div > input"),
                                  max_wait_time=120)

    # Example command
    chat_input.send_keys("I need to run KYC on Deutsche Bank AG domiciled in Germany")
    chat_input.send_keys(Keys.RETURN)

    entity_search = wait_for_element(driver, (By.CSS_SELECTOR, ".fill-primary-green-blue-3"), max_wait_time=120)
    droppable_area = wait_for_element(driver, (By.CSS_SELECTOR, ".react-grid-layout"), max_wait_time=120)

    actions = webdriver.ActionChains(driver)
    actions.drag_and_drop(entity_search, droppable_area).perform()

    time.sleep(1)

    more_button = wait_for_element(driver, (By.CSS_SELECTOR,
                                            r".\!bg-transparent > div:nth-child(1) > div:nth-child(1) > "
                                            r"div:nth-child(2) > button:nth-child(1)"),
                                   max_wait_time=120)
    more_button.click()

    time.sleep(2)

    full_view = wait_for_element(driver, (By.CSS_SELECTOR, "button.text-nowrap:nth-child(2) > span:nth-child(2)"),
                                 max_wait_time=120)
    full_view.click()

    time.sleep(1)

    action_button = wait_for_element(driver, (By.CSS_SELECTOR,
                                              ".max-h-fit > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) "
                                              "> tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > "
                                              "div:nth-child(1)"),
                                     max_wait_time=120)
    action_button.click()

    Adidas_Entity_profile = wait_for_element(driver, (
    By.CSS_SELECTOR, "div.mr-4:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("I want you to build a screening bag for all related to Deutsche Bank")
    chat_input.send_keys(Keys.RETURN)

    Screening_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_4 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("What templates are there in the system right now?")
    chat_input.send_keys(Keys.RETURN)

    Template_management_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_6 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("Now show me which watch lists are maintained in system")
    chat_input.send_keys(Keys.RETURN)

    List_management_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_8 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("One last thing. Can you show me the screening history?")
    chat_input.send_keys(Keys.RETURN)

    Screening_History_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_10 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"),
                                                max_wait_time=120)

    chat_input.send_keys(
        "Can you show me the corporate structure of SCHRAMM HOLDING? I only want to see those with holdings exceeding 5%")
    chat_input.send_keys(Keys.RETURN)

    Corporate_structure_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_13 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("I want to create screening response rule")
    chat_input.send_keys(Keys.RETURN)

    Response_Management_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_15 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("Show me cyber incidents related to this entity in VLA graph")
    chat_input.send_keys(Keys.RETURN)

    Link_Analysi_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_17 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("Can you also search company Deutsche Bank AG for adverse media mentions?")
    chat_input.send_keys(Keys.RETURN)

    Adverse_media_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_19 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

    chat_input.send_keys("I want to screen person Herbert Kauffmann using promtyf.ai-adidas-internal-20240802")
    chat_input.send_keys(Keys.RETURN)

    Screening_Result_widget = wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_21 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"), max_wait_time=120)

except Exception as error:
    print("An error occurred:", error)

finally:
    time.sleep(5)
    profile = wait_for_element(driver, (By.CSS_SELECTOR,
                                        "div.w-full:nth-child(15) > div:nth-child(1) > div:nth-child(1) > "
                                        "div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > "
                                        "button:nth-child(1)"),
                               max_wait_time=120)
    profile.click()
    time.sleep(10)

    log_out = wait_for_element(driver, (By.CSS_SELECTOR, r".bg-\[\#226085\]"), max_wait_time=120)
    # log_out.click()

    time.sleep(20)
    # driver.quit()
