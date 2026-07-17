import pytest
from praktikum.bun import Bun


class TestBun:

    # Один позитивный тест без параметризации
    def test_get_name_returns_name(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"

    def test_get_price_returns_price(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_price() == 100.0

    # Параметризация с разными типами названий и цен
    @pytest.mark.parametrize("name, price", [
        ("bun with spaces", 50.5),        # пробелы, дробная цена
        ("123bun", 0),                    # цифры в названии, нулевая цена
        ("специальный", -10.0),           # кириллица, отрицательная цена
        ("bun!@#", 999.99),              # спецсимволы
        ("a" * 100, 0.01),               # очень длинное название, маленькая цена
    ])
    def test_bun_creation_various_inputs(self, name, price):
        """Проверяем, что Bun создаётся с любыми допустимыми значениями."""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
        