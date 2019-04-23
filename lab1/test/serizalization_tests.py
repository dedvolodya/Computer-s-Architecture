import unittest
from controller import budget_controler
from serialization import common
import os


class TestSerializationMethods(unittest.TestCase):
    user = budget_controler.start_budget_init(100, 'Vasia')

    def setUp(self):
        common.save_user(self.user)

    def test_save1(self):
        f = open("../user-json/Vasia.json", "r")
        self.assertEqual("{\"total\": 100, \"owner\": \"Vasia\"}", f.readline())
        self.assertEqual("", f.readline())
        f.close()

    def test_load1(self):
        new_user = common.load_user(self.user.get_owner())
        self.assertEqual(self.user.get_owner(), new_user.get_owner())
        self.assertEqual(self.user.get_total(), new_user.get_total())
        self.assertEqual(str(self.user.get_statistic()), str(new_user.get_statistic()))

    def tearDown(self):
        os.remove("../user-json/Vasia.json")
        os.remove("../user-json/Vasia_stat.json")


if __name__ == '__main__':
    unittest.main()
