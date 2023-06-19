import pytest
import products

"""
Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception.
"""


def test_create_product_name():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    assert type(xiaomi.name) == str


def test_create_product_price():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    assert xiaomi.price >= 1


def test_create_product_quantity():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    assert xiaomi.quantity >= 0


def test_create_product_active():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    assert type(xiaomi.active) == bool


def test_create_invalid_product():
    invalid_product = products.Product(name=1, price=-200,quantity=0, active=True)
    assert type(invalid_product.name) != str or invalid_product.price < 0


def test_no_inventory():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    xiaomi.buy(137)
    assert xiaomi.is_active() == False


def test_modified_quantity():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    xiaomi.buy(105)
    assert xiaomi.quantity == 32


def test_larger_than_quantity_exception():
    xiaomi = products.Product(name="Xiaomi Poco X3 NFC", price=230, quantity=137, active=True)
    assert xiaomi.buy(170)
    assert xiaomi.quantity == 137


pytest.main()
