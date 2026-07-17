from unittest.mock import patch
from praktikum.praktikum import main


class TestPraktikum:

    @patch('builtins.print')
    def test_main_runs_without_errors(self, mock_print):
        """Проверяем, что main() выполняется без ошибок."""
        main()
        assert mock_print.called

    def test_main_guard(self):
        """Проверяем, что __name__ == '__main__' отрабатывает."""
        import runpy
        runpy.run_module("praktikum.praktikum", run_name="__main__")