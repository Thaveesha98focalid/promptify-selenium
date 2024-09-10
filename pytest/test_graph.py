import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# Pytest fixture to manage WebDriver setup and teardown
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Helper function to wait for an element to appear
def wait_for_element(driver, locator, timeout=10):
    while True:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not found. Retrying...")


# The main test function
def test_selenium_script(driver):
    username = "thaveesha@datafab.ai"
    password = "thaveesha@123"
    login_url = "http://localhost:3000"

    driver.get(login_url)

    # Login process
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

    # Interacting with the chat input
    chat_input = wait_for_element(driver, (By.CSS_SELECTOR,
                                           r"body > div.h-full.w-1\/4.min-w-\[304px\] > div > div > "
                                           r"div.flex-2.overflow-y-auto.p-2 > div > div > input"))

    actions = ActionChains(driver)
    droppable_area = wait_for_element(driver, (By.CSS_SELECTOR, ".react-grid-layout"))

    time.sleep(2)

    chat_input.send_keys("Show me case list per day as diagram, differentiated by type")
    chat_input.send_keys(Keys.RETURN)

    conform_graph = wait_for_element(driver, (By.CSS_SELECTOR,
                                              "#widget_1 > div:nth-child(2) > div:nth-child(1) >"
                                              " div:nth-child(1) > div:nth-child(2)"))

    assert "Transaction Flow" in conform_graph.text

    time.sleep(2)

    actions.drag_and_drop(wait_for_element(driver, (
    By.CSS_SELECTOR, "#widget_1 > div.absolute.right-1\\.5.top-0.z-20.bg-transparent.pb-0\\.5.pt-\\[6\\.5px\\] > svg")),
                          droppable_area).perform()

    graph_dropDown = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) > "
                                                                "div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"
                                                                " > div:nth-child(1)"))
    # dropDown hover
    actions.move_to_element(graph_dropDown).perform()

    # select first element
    first_element = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) > "
                                                               "div:nth-child(1) > div:nth-child(1) > div:nth-child("
                                                               "2) >"
                                                               "div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) >"
                                                               " li:nth-child(1)"))

    first_element.click()

    graph1_conformation = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) >"
                                                                     " div:nth-child(2) > "
                                                                     "div:nth-child(1)")).get_attribute("aria-label")

    assert "gradient_area_chart" in graph1_conformation, f"Test case 1 failed"

    second_element = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) > "
                                                                "div:nth-child(1) > div:nth-child(1) > div:nth-child("
                                                                "2) >div:nth-child(1) > div:nth-child(2) >"
                                                                " ul:nth-child(1) > li:nth-child(2)"))

    time.sleep(2)

    second_element.click()

    graph2_conformation = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) >"
                                                                     " div:nth-child(2) >"
                                                                     " div:nth-child(1)")).get_attribute("aria-label")

    assert "large_scale_area_chart" in graph2_conformation, f"Test case 2 failed"

    third_element = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) > "
                                                               "div:nth-child(1) > div:nth-child(1) > "
                                                               "div:nth-child(2) > div:nth-child(1) > "
                                                               "div:nth-child(2) > ul:nth-child(1) > li:nth-child(3)"))

    time.sleep(2)

    third_element.click()

    graph3_conformation = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) >"
                                                                     " div:nth-child(2) >"
                                                                     " div:nth-child(1)")).get_attribute("aria-label")

    assert "background_bar_chart" in graph3_conformation, f"Test case 3 failed"

    time.sleep(2)

    fourth_element = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) >"
                                                                " div:nth-child(1) > div:nth-child(1) >"
                                                                " div:nth-child(2) > div:nth-child(1) > "
                                                                "div:nth-child(2) > ul:nth-child(1) > li:nth-child(4)"))

    fourth_element.click()

    graph4_conformation = wait_for_element(driver, (By.CSS_SELECTOR, ".blur-fix-wrapper > div:nth-child(1) >"
                                                                     " div:nth-child(2) >"
                                                                     " div:nth-child(1)")).get_attribute("aria-label")

    assert "bar_animation_delay" in graph4_conformation, f"Test case 4 failed"

    time.sleep(10)

