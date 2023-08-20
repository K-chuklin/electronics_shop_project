import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('NuPhy Air75', 14300, 1)


def test_init(keyboard1):
    assert keyboard1.name == 'NuPhy Air75'
    assert keyboard1.price == 14_300
    assert keyboard1.amount == 1


def test_lang(keyboard1):
    assert str(keyboard1.language) == "EN"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"


def test_change_lang(keyboard1):
    assert str(keyboard1.change_lang()) == "RU"


def test_change_lang2(keyboard1):
    try:
        keyboard1.language == "KZ"
    except:
        return AttributeError