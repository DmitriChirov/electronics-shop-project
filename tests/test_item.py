"""Здесь тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def testing_item():
    return Item('Образец', 100, 5)


def test_item_init(testing_item):
    """Когда мы создаем экземпляр класса со значениями 'Тестовый образец', 100, 5, то вызов атрибутов вернет соответствующие значения"""
    assert testing_item.name == 'Образец'
    assert testing_item.price == 100
    assert testing_item.quantity == 5


def test_apply_discount(testing_item):
    """Когда мы создаем класс со значением 'Образец', 100, 5, затем вызываем apply_discount, то price изменится в pay_rate раз"""
    testing_item.pay_rate = 0.5
    testing_item.apply_discount()
    assert testing_item.price == 50


def test_calculate_total_price(testing_item):
    """Когда мы вызываем calculate_total_price, то получаем общую стоимость имеющегося товара"""
    assert testing_item.calculate_total_price() == 500


def test_item_repr(testing_item):
    """Когда мы вызываем __repr__, то получаем строку с информацией о товаре"""
    assert repr(testing_item) == "Item('Образец', 100, 5)"


def test_item_str(testing_item):
    """Когда мы вызываем __str__, то получаем строку с информацией о товаре"""
    assert str(testing_item) == "Образец"


def test_name(testing_item):
    """Когда мы вызываем name, то получаем имя товара, когда передаем аргументом новое имя, то имя товара изменяется"""
    assert testing_item.name == 'Образец'
    testing_item.name = 'Суперсмартфон'
    assert testing_item.name == 'Суперсмарт'
