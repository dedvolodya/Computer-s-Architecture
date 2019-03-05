import pickle
from logic import budget


class PickleSerialize:
    @staticmethod
    def save(obj, filename):
        """serialize Budget instance into file"""
        with open(filename + ".pkl", "wb") as f:
            pickle.dump(obj, f)
        with open(filename + "stat.pkl", "wb") as f:
            pickle.dump(obj.get_statistic(), f)

    @staticmethod
    def load(filename):
        """"deserialize instance"""
        with open(filename + ".pkl", "rb") as f:
            obj = pickle.load(f)
        with open(filename + "stat.pkl", "rb") as f:
            return budget.Budget(obj.get_total(), obj.get_owner(), pickle.load(f))
