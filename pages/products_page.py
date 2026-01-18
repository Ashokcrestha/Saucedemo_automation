from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    ADD_TO_CART = (By.CLASS_NAME, "btn_inventory")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_first_n_product_names(self, count=3):
        names = self.driver.find_elements(*self.PRODUCT_NAME)
        return [names[i].text for i in range(count)]

    def add_products_by_count(self, count=3):
        for i in range(count):
            # Locate the buttons freshly each time (important!)
            buttons = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.ADD_TO_CART)
            )
            buttons[i].click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
