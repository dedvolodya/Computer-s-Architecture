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


class JSONSerialize:

    @staticmethod
    def save(obj, filename):
        """serialize Budget instance into file"""
        f1 = open(filename + ".json", 'w')
        json.dump(obj, f1, default=lambda o: o.__dict__)
        f2 = open(filename + "stat.json", 'w')
        json.dump(datetime_key_fix(obj.get_statistic()), f2)
        f1.close()
        f2.close()

    @staticmethod
    def load(filename):
        """"deserialize instance"""
        f1 = open(filename + ".json", "r")
        obj = json.load(f1)
        f2 = open(filename + "stat.json", "r")
        stat = json.load(f2)
        f1.close()
        f2.close()
        return budget.Budget(obj["total"], obj["owner"], stat)
