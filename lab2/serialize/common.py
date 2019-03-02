from lab2.serialize import pickle_serialize
from lab2.serialize import yaml_serialize
from lab2.serialize import json_serialize
serialization_type = 1


def save_user(user):
    """common procedure to serialize by given type"""
    if serialization_type == 1:
        pickle_serialize.save(user, "../user-pickle")
    elif serialization_type == 2:
        yaml_serialize.save(user, "../user-yaml")
    elif serialization_type == 3:
        json_serialize.save(user, "../user-json")


def load_user():
    """common deserialize function"""
    if serialization_type == 1:
        return pickle_serialize.load("../user-pickle")
    elif serialization_type == 2:
        return yaml_serialize.load("../user-yaml")
    elif serialization_type == 3:
        return json_serialize.load("../user-json")
