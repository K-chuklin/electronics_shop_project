import pytest
from homework_1.src.item import Item


item1 = Item("Смартфон", 10000, 20)


def test_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.amount == 20


def test_calculate_total_price():
    assert item1.calculate_total_price() == '200000'


def test_apply_discount():
    assert item1.apply_discount() is None
