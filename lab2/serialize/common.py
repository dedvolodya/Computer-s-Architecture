from serialize import pickle_serialize
from serialize import yaml_serialize
from serialize import json_serialize
from configs import config_reader


def save_user(user):
    """common procedure to serialize by given type"""
    config = config_reader.read_config()
    serialization_type = int(config.get('Serialization', 'type'))
    path = config.get('Serialization', 'path')
    if serialization_type == 1:
        pickle_serialize.save(user, path)
    elif serialization_type == 2:
        yaml_serialize.save(user, path)
    elif serialization_type == 3:
        json_serialize.save(user, path)


def load_user():
    """common deserialize function"""
    config = config_reader.read_config()
    serialization_type = int(config.get('Serialization', 'type'))
    path = config.get('Serialization', 'path')
    if serialization_type == 1:
        return pickle_serialize.load(path)
    elif serialization_type == 2:
        return yaml_serialize.load(path)
    elif serialization_type == 3:
        return json_serialize.load(path)
