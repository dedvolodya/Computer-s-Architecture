import unittest
from controller import budget_controler
from logic import budget


def expected_result_list_init():
    result = [100, 300, 200]
    return result


def simple_budget_operations(init_total):
    current_budget = budget.Budget(init_total, "Jim")
    current_budget.inc_total(200)
    current_budget.dec_total(100)
    return current_budget


class TestLogicMethods(unittest.TestCase):

    def test_menu_item_correct(self):
        self.assertEqual(None, budget_controler.is_menu_item_correct(0))
        self.assertEqual(True, budget_controler.is_menu_item_correct(3))
        self.assertEqual(None, budget_controler.is_menu_item_correct(7))

    def test_init_1(self):
        init_total = 100
        init_name = "Jim"
        current_budget = budget.Budget(init_total, init_name)
        total = current_budget.get_total()
        name = current_budget.get_owner()
        self.assertEqual(total, init_total)
        self.assertEqual(name, init_name)

    def test_inc_dec(self):
        init_total = 100
        current_budget = simple_budget_operations(init_total)
        expected_result = init_total * 2
        self.assertEqual(current_budget.get_total(), expected_result)

    def test_budget_stat(self):
        init_total = 100
        current_budget = simple_budget_operations(init_total)
        budget_holder = current_budget.get_statistic()
        result = []
        for key in budget_holder:
            result.append(int(budget_holder[key]))
        expected_result = expected_result_list_init()
        self.assertListEqual(result, expected_result)

    def test_fail_init(self):
        try:
            budget.Budget(-1, "Jim")

        except ValueError as e:
            self.assertEqual(str(e), "Incorrect total value!")

    def test_fail_inc(self):
        user = budget.Budget(100, 'Jim')
        try:
            user.inc_total(-10)
        except ValueError as e:
            self.assertEqual(str(e), "Incorrect total value!")

    def test_fail_dec(self):
        user = budget.Budget(100, 'Jim')
        try:
            user.dec_total(-10)
        except ValueError as e:
            self.assertEqual(str(e), "Incorrect total value!")


if __name__ == '__main__':
    unittest.main()
