import yaml
from lab2.logic import budget


def save(obj, filename):
    """serialize Budget instance into file"""
    f1 = open(filename + ".yml", 'w')
    yaml.dump(obj, f1,default_flow_style=False)
    f2 = open(filename + "stat.yml", 'w')
    yaml.dump(obj.get_statistic(), f2, default_flow_style=False)


def load(filename):
    """"deserialize instance"""
    f1 = open(filename + ".yml", "r")
    obj = yaml.load(f1)
    f2 = open(filename + "stat.yml", "r")
    return budget.Budget(obj.get_total(), obj.get_owner(), yaml.load(f2))
