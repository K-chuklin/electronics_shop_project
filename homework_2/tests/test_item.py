import pytest
from homework_2.src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 2)


def test_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.amount == 2


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == '20000'


def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item1.apply_discount() is None


def test_name(item1):
    item1.name = 'Суперсмартфон'
    assert item1.name == 'Суперсмарт'


def test_repr(item1):
    assert repr(item1) == 'Смартфон, 10000, 2'


def test_str(item1):
    assert str(item1) == 'В магазине есть товар с именем Смартфон, стоимостью 10000 и в количестве 2 шт.'
