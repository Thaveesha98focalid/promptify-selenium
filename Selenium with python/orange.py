from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox()
def wait_for_element(driver, locator, timeout=10):
    while True:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not found. Retrying...")


driver.maximize_window()

username = "thaveesha@datafab.ai"
password = "thaveesha@123"

login_url = "http://localhost:3000"
driver.get(login_url)

try:
    username_field = wait_for_element(driver, (By.XPATH, "//input[@type='text']"))
    username_field.send_keys(username)

    password_field = wait_for_element(driver, (By.XPATH, "//input[@type='password']"))
    password_field.send_keys(password)

    login_button = wait_for_element(driver, (By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/button"))
    login_button.click()

    success_element = wait_for_element(driver, (By.CSS_SELECTOR,
                                                r"body > div.h-full.w-1\/4.min-w-\[304px\] > div > div > "
                                                r"div.extend-beyond-borders.w-full.p-0 > div > "
                                                r"div.flex.w-full.flex-row.items-center.justify-start > "
                                                r"div.text-nowrap.bg-transparent.p-\[5px\].px-\["
                                                r"8px\].text-sm.font-medium.text-green-blue-2"))

    assert "Prompt" in success_element.text

    chat_command_01 = "I need to run KYC on Orange domiciled in France"
    chat_command_04 = "I want you to build a screening bag for all entities related to Orange"
    chat_command_05 = "What templates are there in the system right now?"
    chat_command_06 = "Now show me which watch lists are maintained in system"
    chat_command_07 = "One last thing. Can you show me the screening history?"
    chat_command_08 = ("Can you show me the corporate structure of Orange? I only want to see those with holdings "
                       "exceeding 1%")
    chat_command_09 = " I want to create screening response rule"
    chat_command_10 = "Show me cyber incidents related to this entity in VLA graph"
    chat_command_11 = "Can you also search company Orange for adverse media mentions?"
    # chat_command_11_1 = "Can you also search company mbank for adverse media mentions?"
    chat_command_12 = "I want to screen person Herbert Kauffmann using promtyf.ai-adidas-internal-20240802"
    # chat_command_13 = "i want the map of adidas office locations"

    chat_input = wait_for_element(driver, (By.CSS_SELECTOR,
                                           r"body > div.h-full.w-1\/4.min-w-\[304px\] > div > div > "
                                           r"div.flex-2.overflow-y-auto.p-2 > div > div > input"))

    time.sleep(1)

    chat_input.send_keys(chat_command_01)
    chat_input.send_keys(Keys.RETURN)

    entity_search = wait_for_element(driver, (By.CSS_SELECTOR, ".fill-primary-green-blue-3"))
    droppable_area = wait_for_element(driver, (By.CSS_SELECTOR, ".react-grid-layout"))

    actions = ActionChains(driver)
    actions.drag_and_drop(entity_search, droppable_area).perform()

    time.sleep(1)

    entity_search_more_button = wait_for_element(driver, (By.CSS_SELECTOR,
                                                          r".\!bg-transparent > div:nth-child(1) > "r"div:nth-child("
                                                          r"1) > div:nth-child(2) > button:nth-child(1)"))
    entity_search_more_button.click()

    time.sleep(2)

    entity_search_full_view = wait_for_element(driver,
                                               (By.CSS_SELECTOR, "button.text-nowrap:nth-child(2) > span:nth-child(2)"))
    entity_search_full_view.click()

    time.sleep(1)

    entity_search_action_button = wait_for_element(driver, (By.CSS_SELECTOR,
                                                            ".max-h-fit > div:nth-child(1) > div:nth-child(1) > "
                                                            "table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("
                                                            "1) > td:nth-child(4) > div:nth-child(1)"))
    entity_search_action_button.click()
    time.sleep(1)

    entity_search_more_button.click()
    time.sleep(1)

    entity_search_minimal_view = wait_for_element(driver, (By.CSS_SELECTOR, "button.text-nowrap:nth-child(3)"))
    entity_search_minimal_view.click()

    entity_profile = wait_for_element(driver, (
     By.CSS_SELECTOR, "div.mr-4:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))

    entity_profile_dragBtn = wait_for_element(driver, (
     By.CSS_SELECTOR, r"#widget_2 > div.absolute.right-1\.5.top-0.z-20.bg-transparent.pb-0\.5.pt-\[6\.5px\] > svg"))
    time.sleep(1)

    actions.drag_and_drop(entity_profile_dragBtn, droppable_area).perform()

    chat_input.send_keys(chat_command_04)
    time.sleep(1)

    chat_input.send_keys(Keys.RETURN)

    Screening_widget = wait_for_element(driver, (
     By.CSS_SELECTOR, "#widget_4 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))

    im_widget_dropDown_icon = wait_for_element(driver, (By.CSS_SELECTOR, "button.p-2:nth-child(3)"))
    im_widget_dropDown_icon.click()
    time.sleep(1)

    screening_widget_draggable_icon = wait_for_element(driver, (By.CSS_SELECTOR, "#widget_4 > div:nth-child(1)"))
    actions.drag_and_drop(screening_widget_draggable_icon, droppable_area).perform()

    chat_input.send_keys(chat_command_05)
    time.sleep(1)

    chat_input.send_keys(Keys.RETURN)

    Template_management_widget = wait_for_element(driver, (By.CSS_SELECTOR, "#widget_6 > div:nth-child(2) >"
                                                                            " div:nth-child(1) > div:nth-child(2)"))

    time.sleep(1)

    Template_management_widget_draggable_icon = wait_for_element(driver, (By.CSS_SELECTOR, "#widget_6 > "
                                                                                           "div:nth-child(1)"))
    actions.drag_and_drop(Template_management_widget_draggable_icon, droppable_area).perform()
    time.sleep(1)

    chat_input.send_keys(chat_command_06)
    time.sleep(1)

    chat_input.send_keys(Keys.RETURN)

    List_management_widget = wait_for_element(driver, (
     By.CSS_SELECTOR, "#widget_8 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))

    time.sleep(1)
    entity_search_more_button.click()
    entity_search_close_button = wait_for_element(driver, (By.CSS_SELECTOR, "button.text-left:nth-child(1)"))
    entity_search_close_button.click()

    time.sleep(1)

    list_management_widget_draggable_icon = wait_for_element(driver, (By.CSS_SELECTOR, "#widget_8 > div:nth-child(1)"))
    actions.drag_and_drop(list_management_widget_draggable_icon, droppable_area).perform()
    time.sleep(1)

    chat_input.send_keys(chat_command_07)
    time.sleep(1)

    chat_input.send_keys(Keys.RETURN)
    #
    # Screening_History_widget = wait_for_element(driver, (
    # By.CSS_SELECTOR, "#widget_10 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"))
    #
    # chat_input.send_keys(chat_command_08)
    # time.sleep(1)
    #
    # chat_input.send_keys(Keys.RETURN)
    #
    # Corporate_structure_widget = wait_for_element(driver, (
    # By.CSS_SELECTOR, "#widget_13 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
    #
    # chat_input.send_keys(chat_command_09)
    # time.sleep(1)
    #
    # chat_input.send_keys(Keys.RETURN)
    #
    # Response_Management_widget = wait_for_element(driver, (
    #     By.CSS_SELECTOR, "#widget_15 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
    #
    # chat_input.send_keys(chat_command_10)
    # time.sleep(1)
    #
    # chat_input.send_keys(Keys.RETURN)
    #
    # Link_Analysi_widget = wait_for_element(driver, (
    #     By.CSS_SELECTOR, "#widget_17 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
    #
    # chat_input.send_keys(chat_command_11)
    # time.sleep(1)
    #
    # chat_input.send_keys(Keys.RETURN)
    #
    # Adverse_media_widget = wait_for_element(driver, (
    #     By.CSS_SELECTOR, "#widget_19 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
    #
    # chat_input.send_keys(chat_command_12)
    # time.sleep(1)
    #
    # chat_input.send_keys(Keys.RETURN)
    #
    # Screening_Result_widget = wait_for_element(driver, (
    #     By.CSS_SELECTOR, "#widget_21 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))

except Exception as error:
    print("An error occurred:", error)

finally:
    time.sleep(5)
    profile = wait_for_element(driver, (By.CSS_SELECTOR,
                                        "div.w-full:nth-child(15) > div:nth-child(1) > div:nth-child(1) > "
                                        "div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > "
                                        "button:nth-child(1)"))
    profile.click()
    time.sleep(10)

    log_out = wait_for_element(driver, (By.CSS_SELECTOR, r".bg-\[\#226085\]"))
    log_out.click()

    time.sleep(20)
    # driver.quit()
