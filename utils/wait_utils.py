import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def grace_wait(seconds=3):
    """
    Grace wait for observation / manual cancel
    """
    time.sleep(seconds)
