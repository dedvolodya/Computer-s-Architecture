import json
from logic import budget


def save(obj, filename):
    """serialize Budget instance into file"""
    f1 = open(filename + "/" + obj.get_owner() + ".json", 'w+')
    json.dump(obj, f1, default=lambda o: o.__dict__)
    f2 = open(filename + "/" + obj.get_owner() + "_stat.json", 'w+')
    json.dump(str(obj.get_statistic()), f2)


def load(filename):
    """"deserialize instance"""
    f1 = open(filename + ".json", "r")
    obj = json.load(f1)
    f2 = open(filename + "_stat.json", "r")
    stat = json.load(f2)
    return budget.Budget(int(obj["total"]), obj["owner"], stat)
