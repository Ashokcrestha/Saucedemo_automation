import pytest
import csv
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.bug_reporter import log_bug
from utils.wait_utils import grace_wait


def load_users():
    with open("data/login_data.csv") as f:
        return list(csv.DictReader(f))


@pytest.mark.parametrize("user", load_users())
def test_e2e_all_users(driver, user):

    if user["expected"] == "locked":
        pytest.skip("Locked user")

    # 🔹 Login
    login = LoginPage(driver)
    login.open()
    login.login(user["username"], user["password"])
    assert "inventory" in driver.current_url

    # 🔹 Add multiple products
    products = ProductsPage(driver)

    item_count = 3  # ✅ change this number to add more items
    expected_names = products.get_first_n_product_names(item_count)
    products.add_products_by_count(item_count)

    grace_wait(3)

    # 🔹 Go to cart
    products.go_to_cart()
    grace_wait(2)

    cart = CartPage(driver)

    # 🔹 Verify cart items count
    assert cart.get_cart_items_count() == item_count

    # 🔹 Verify cart items names
    assert cart.get_cart_items_names() == expected_names

    # 🔹 Checkout (attempt only)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout_success = checkout.try_checkout()

    if not checkout_success:
        log_bug(
            "Checkout Failure",
            f"Checkout failed for {user['username']}",
            "Medium",
            "P2"
        )

    checkout.logout()
