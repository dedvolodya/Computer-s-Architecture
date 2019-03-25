from serialization import json_serialize

serialization_type = 1


def save_user(user):
    """common procedure to serialize by given type"""
    if serialization_type == 1:
        json_serialize.save(user, "../user-json")


def load_user(name):
    """common deserialize function"""
    if serialization_type == 1:
        return json_serialize.load("../user-json/" + name)
