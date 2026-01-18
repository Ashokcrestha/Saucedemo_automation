from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element

class CartPage:
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        wait_for_element(self.driver, self.CART_ITEM, timeout=10)
        return self.driver.find_elements(*self.CART_ITEM)

    def get_cart_items_count(self):
        return len(self.get_cart_items())

    def get_cart_items_names(self):
        return [item.text for item in self.get_cart_items()]

    def proceed_to_checkout(self):
        wait_for_element(self.driver, self.CHECKOUT_BTN, timeout=10)
        self.driver.find_element(*self.CHECKOUT_BTN).click()
