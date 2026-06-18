import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "cutlet"
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_price.return_value = 100.0

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        mock1 = Mock()
        mock2 = Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock2

    def test_move_ingredient_moves_correctly(self):
        burger = Burger()
        mock1 = Mock()
        mock2 = Mock()
        mock3 = Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock2
        assert burger.ingredients[1] == mock3
        assert burger.ingredients[2] == mock1

    def test_get_price_returns_correct_sum(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50.0
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75.0

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        # Цена = булка * 2 + ингредиенты = 200 + 50 + 75 = 325
        assert burger.get_price() == 325.0

    def test_get_receipt_returns_correct_format(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "cutlet"
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 300.0"
        )

        assert receipt == expected

    @pytest.mark.parametrize("bun_price, ing1_price, ing2_price, expected_total", [
        (100.0, 50.0, 75.0, 325.0),
        (200.0, 100.0, 150.0, 650.0),
        (50.0, 25.0, 25.0, 150.0),
    ])
    def test_get_price_parametrized(self, bun_price, ing1_price, ing2_price, expected_total):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = ing1_price
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = ing2_price

        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        assert burger.get_price() == expected_total