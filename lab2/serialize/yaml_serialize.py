import yaml
from logic import budget


class YamlSerialize:

    @staticmethod
    def save(obj, filename):
        """serialize Budget instance into file"""
        f1 = open(filename + ".yml", 'w')
        yaml.dump(obj, f1, default_flow_style=False)
        f2 = open(filename + "stat.yml", 'w')
        yaml.dump(obj.get_statistic(), f2, default_flow_style=False)
        f1.close()
        f2.close()

    @staticmethod
    def load(filename):
        """"deserialize instance"""
        f1 = open(filename + ".yml", "r")
        obj = yaml.load(f1)
        f2 = open(filename + "stat.yml", "r")
        f1.close()
        statistic = yaml.load(f2)
        f2.close()
        return budget.Budget(obj.get_total(), obj.get_owner(), statistic)
