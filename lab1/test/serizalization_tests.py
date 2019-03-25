import io
import unittest
from controller import budget_controler
from logic.budget import Budget
from serialization import common
from configs import config_reader


class TestSerializationMethods(unittest.TestCase):
    user: Budget = budget_controler.start_budget_init(100, 'Vasia')

    def test_save1(self):
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(1)
        serializator = common.Serializator(config_read)
        serializator.save_user(self.user)
        f = open("../user.pkl", "rb")
        expected = io.BytesIO(b"\x80\x03")
        self.assertEqual(str(expected.getvalue()), str(f.read(io.SEEK_END)))
        f.close()

    def test_save2(self):
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(2)
        serializator = common.Serializator(config_read)
        serializator.save_user(self.user)
        f = open("../user.yml", "r")
        self.assertEqual("!!python/object:logic.budget.Budget\n", f.readline())
        self.assertEqual("owner: Vasia\n", f.readline())
        self.assertEqual("total: 100\n", f.readline())
        self.assertEqual("", f.readline())
        f.close()

    def test_save3(self):
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(3)
        serializator = common.Serializator(config_read)
        serializator.save_user(self.user)
        f = open("../user.json", "r")
        self.assertEqual("{\"total\": 100, \"owner\": \"Vasia\"}", f.readline())
        self.assertEqual("", f.readline())
        f.close()

    def test_load1(self):
        user = budget_controler.start_budget_init(100, 'Vasia')
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(1)
        serializator = common.Serializator(config_read)
        serializator.save_user(user)
        new_user = serializator.load_user()
        self.assertEqual(user.get_owner(), new_user.get_owner())
        self.assertEqual(user.get_total(), new_user.get_total())
        self.assertEqual(user.get_statistic(), new_user.get_statistic())

    def test_load2(self):
        user = budget_controler.start_budget_init(100, 'Vasia')
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(2)
        serializator = common.Serializator(config_read)
        serializator.save_user(user)
        new_user = serializator.load_user()
        self.assertEqual(user.get_owner(), new_user.get_owner())
        self.assertEqual(user.get_total(), new_user.get_total())
        self.assertEqual(user.get_statistic(), new_user.get_statistic())

    def test_load3(self):
        config_read = config_reader.ConfigReader("../configs/config.ini")
        config_read.set_type(3)
        serializator = common.Serializator(config_read)
        serializator.save_user(self.user)
        new_user = serializator.load_user()
        self.assertEqual(self.user.get_owner(), new_user.get_owner())
        self.assertEqual(self.user.get_total(), new_user.get_total())
        self.assertEqual(self.user.get_statistic(), new_user.get_statistic())


if __name__ == '__main__':
    unittest.main()