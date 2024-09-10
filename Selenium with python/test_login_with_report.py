import pytest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    # driver.quit()


def wait_for_element(driver, locator, timeout=10):
    while True:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not found. Retrying...")


@pytest.mark.parametrize("email,password,expected_result", [
    ("wrongemail@datafab.ai", "thaveesha@123", "Login Failed"),
    ("wrongemail@datafab.ai", "wrongpassword", "Login Failed"),
    ("thaveesha@datafab.ai", "thaveesha@123", "Login success"),
    ("thaveesha@datafab.ai", "wrongpassword", "Login Failed"),
])
def test_login(driver, email, password, expected_result):
    driver.get("https://promptify.datafabdevelopment.com/")

    time.sleep(1)
    username_field = wait_for_element(driver, (By.CSS_SELECTOR, "input[placeholder='Username']"))
    password_field = wait_for_element(driver, (By.CSS_SELECTOR, "input[placeholder='Password']"))
    login_button = wait_for_element(driver, (By.CSS_SELECTOR, "body div div div div button"))

    username_field.send_keys(email)
    password_field.send_keys(password)
    time.sleep(2)
    login_button.click()

    if expected_result == "Login success":
        time.sleep(1)
        success_element = driver.find_element(By.CSS_SELECTOR, "body > div.h-full.w-1\/4.min-w-\[304px\] > div > div "
                                                               "> div.extend-beyond-borders.w-full.p-0 > div >"
                                                               " div.flex.w-full.flex-row.items-center.justify-start >"
                                                               "div.relative.text-nowrap.bg-transparent.p-\["
                                                               "5px\].px-\["
                                                               "8px\].text-sm.font-medium.capitalize.text-green-blue-2")

        assert success_element is not None, "Login failed."

        profile = wait_for_element(driver, (By.CSS_SELECTOR,
                                            "div.rounded-6:nth-child(2) > div:nth-child(2) > button:nth-child(1)"))
        profile.click()
        time.sleep(1)

        log_out = wait_for_element(driver, (By.CSS_SELECTOR, r".bg-\[\#226085\]"))
        log_out.click()


    else:
        error_message = driver.find_element(By.CSS_SELECTOR, ".text-\[40px\]")
        assert error_message is not None, "Expected login to fail but it succeeded."
