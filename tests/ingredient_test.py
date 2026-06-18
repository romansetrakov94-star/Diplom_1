import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    # Позитивные тесты без параметризации
    def test_get_type_returns_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name_returns_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)
        assert ingredient.get_name() == "cutlet"

    def test_get_price_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200.0)
        assert ingredient.get_price() == 200.0

    # Параметризация с разными типами, названиями и ценами
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0),
        (INGREDIENT_TYPE_FILLING, "cheese", 50.5),
        (INGREDIENT_TYPE_SAUCE, "sauce with spaces", 0.0),
        (INGREDIENT_TYPE_FILLING, "123filling", -5.0),
        (INGREDIENT_TYPE_SAUCE, "соус", 0.01),
        (INGREDIENT_TYPE_FILLING, "!@#$%", 999.99),
        (INGREDIENT_TYPE_SAUCE, "a" * 50, 100.0),
    ])
    def test_ingredient_creation_various_inputs(self, ingredient_type, name, price):
        """Проверяем, что Ingredient создаётся с разными значениями."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
        