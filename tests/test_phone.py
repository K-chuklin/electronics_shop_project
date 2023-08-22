from unittest.mock import Mock
from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 2)


def test_init(phone1):
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120_000
    assert phone1.amount == 5
    assert phone1.number_of_sim == 2


def test_number_of_sim(phone1):
    try:
        phone1.number_of_sim = 0
    except:
        return ValueError


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone1):
    assert str(phone1) == 'iPhone 14'


def test_add_phone_and_item(item1, phone1):
    total_items = phone1 + item1
    assert total_items == (phone1.amount + item1.amount)


def test_add_item_and_phone(item1, phone1):
    total_items = item1 + phone1
    assert total_items == (item1.amount + phone1.amount)


def test_add_item_and_not_item(item1):
    err_msg = 'Складывать можно только объекты Item и дочерние от них.'
    not_item = Mock()

    with pytest.raises(ValueError, match=err_msg):
        _ = item1 + not_item
