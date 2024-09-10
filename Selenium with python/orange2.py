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

login_url = "https://promptify.datafabdevelopment.com/"
driver.get(login_url)


def drag_element(widget_order):
    css_selector = (
        f"#widget_{widget_order} > div.absolute.right-1\\.5.top-0.z-20.bg-transparent."
        "pb-0\\.5.pt-\\[6\\.5px\\] > svg"
    )
    return wait_for_element(driver, (By.CSS_SELECTOR, css_selector))


def more_button(widget_order):
    css_selector = (
        f"#widget_{widget_order} > div.blur-fix-wrapper.size-full.py-1.pr-1 > "
        f"div.mr-4.flex.w-full.items-start.justify-between.p-[5px].px-[8px].pr-4.pt-[5.1px] > "
        f"div.relative.z-50.mr-1 > button"
    )
    wait_for_element(driver, (By.CSS_SELECTOR, css_selector))


def close(widget_order):
    css_selector = (
        f"#widget_{widget_order} > div.blur-fix-wrapper.size-full.py-1.pr-1 > "
        f"div.mr-4.flex.w-full.items-start.justify-between.p-[5px].px-[8px].pr-4.pt-[5.1px] > "
        f"div.relative.z-50.mr-1 > div > div > "
        f"button.flex.items-center.text-left.text-xs.transition-all.duration-300.hover\\:text-red-4"
    )
    wait_for_element(driver, (By.CSS_SELECTOR, css_selector))


def full_view(widget_order):
    css_selector = (
        f"#widget_{widget_order} > div.blur-fix-wrapper.size-full.py-1.pr-1 > "
        f"div.mr-4.flex.w-full.items-start.justify-between.p-[5px].px-[8px].pr-4.pt-[5.1px] > "
        f"div.relative.z-50.mr-1 > div > div > button:nth-child(2)"
    )
    wait_for_element(driver, (By.CSS_SELECTOR, css_selector))


def minimal_view(widget_order):
    css_selector = (
        f"#widget_{widget_order} > div.blur-fix-wrapper.size-full.py-1.pr-1 > "
        f"div.mr-4.flex.w-full.items-start.justify-between.p-[5px].px-[8px].pr-4.pt-[5.1px] > "
        f"div.relative.z-50.mr-1 > div > div > button:nth-child(3)"
    )
    wait_for_element(driver, (By.CSS_SELECTOR, css_selector))


try:
    username_field = wait_for_element(driver, (By.CSS_SELECTOR, "div.flex-row:nth-child(2) > input:nth-child(1)"))
    username_field.send_keys(username)

    password_field = wait_for_element(driver, (By.CSS_SELECTOR, "div.flex:nth-child(3) > input:nth-child(1)"))
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

    actions = ActionChains(driver)
    droppable_area = wait_for_element(driver, (By.CSS_SELECTOR, ".react-grid-layout"))
    time.sleep(1)

    chat_input.send_keys(chat_command_01)
    chat_input.send_keys(Keys.RETURN)

    entity_search = wait_for_element(driver, (By.CSS_SELECTOR, ".fill-primary-green-blue-3"))
    time.sleep(1)

    actions.drag_and_drop(drag_element(1), droppable_area).perform()

    time.sleep(1)

    wait_for_element(driver, (By.CSS_SELECTOR, ".max-h-fit > div:nth-child(1) > div:nth-child(1) > "
                                               "table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > "
                                               "td:nth-child(4) > div:nth-child(1) > svg:nth-child(1)")).click()

    time.sleep(1)

    entity_profile = wait_for_element(driver, (By.CSS_SELECTOR, "div.mr-4:nth-child(2) > div:nth-child(1) > "
                                                                "div:nth-child(2)"))
    time.sleep(1)

    actions.drag_and_drop(drag_element(2), droppable_area).perform()
    time.sleep(1)

    chat_input.send_keys(chat_command_04)
    chat_input.send_keys(Keys.RETURN)

    screening_bag =wait_for_element(driver, (By.CSS_SELECTOR, "#widget_4 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
    time.sleep(1)

    wait_for_element(driver, (By.CSS_SELECTOR, "button.p-2:nth-child(3)")).click()
    time.sleep(1)

    actions.drag_and_drop(drag_element(4), droppable_area).perform()
    time.sleep(1)


except Exception as error:
    print("An error occurred:", error)
