from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.wait_utils import wait_for_element, grace_wait

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def try_checkout(self):
        try:
            wait_for_element(self.driver, self.FIRST_NAME, timeout=15).send_keys("Test")
            self.driver.find_element(*self.LAST_NAME).send_keys("User")
            self.driver.find_element(*self.POSTAL_CODE).send_keys("12345")
            self.driver.find_element(*self.CONTINUE).click()

            grace_wait(2)

            wait_for_element(self.driver, self.FINISH, timeout=15).click()
            wait_for_element(self.driver, self.COMPLETE_HEADER, timeout=15)

            return True

        except TimeoutException:
            grace_wait(3)
            return False

    def logout(self):
        wait_for_element(self.driver, self.MENU, timeout=10).click()
        grace_wait(2)
        wait_for_element(self.driver, self.LOGOUT, timeout=10).click()
