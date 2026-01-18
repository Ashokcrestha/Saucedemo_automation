import pytest
import csv
from pages.login_page import LoginPage
from utils.bug_reporter import log_bug

def get_test_data():
    with open("data/login_data.csv") as f:
        return list(csv.DictReader(f))

@pytest.mark.parametrize("data", get_test_data())
def test_login(driver, data):
    login = LoginPage(driver)
    login.open()
    login.login(data["username"], data["password"])

    if data["expected"] == "locked":
        try:
            assert "Epic sadface" in login.get_error_message()
        except:
            log_bug("Login Test", "Locked user logged in", "High", "P1")
            raise
    else:
        assert "inventory" in driver.current_url
