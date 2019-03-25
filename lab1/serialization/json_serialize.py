import json
from logic import budget
import datetime


def datetime_key_fix(o):
    if isinstance(o, dict):
        for key in o:
            o[key] = datetime_key_fix(o[key])
            if type(key) is datetime.datetime:
                o[key.isoformat()] = o[key]
                del o[key]
    return o


def save(obj, filename):
    """serialize Budget instance into file"""
    f1 = open(filename + ".json", 'w')
    json.dump(obj, f1, default=lambda o: o.__dict__)
    f2 = open(filename + "stat.json", 'w')
    json.dump(datetime_key_fix(obj.get_statistic()), f2)


def load(filename):
    """"deserialize instance"""
    f1 = open(filename + ".json", "r")
    obj = json.load(f1)
    f2 = open(filename + "stat.json", "r")
    stat = json.load(f2)
    return budget.Budget(obj["owner"], obj["total"], stat)
