import pytest
from utils.driver_factory import get_driver
import time

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    time.sleep(4)  # ⏳ keeps browser open before closing
    driver.quit()
