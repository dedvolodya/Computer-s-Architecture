from serialize import json_serialize
from serialize import pickle_serialize
from serialize import yaml_serialize


class Serializator:
    def __init__(self, config_init):
        self.config_reader = config_init
        config = config_init.read_config()
        serialization_type = int(config.get('Serialization', 'type'))
        if serialization_type == 1:
            self.serializator_impl = pickle_serialize.PickleSerialize
        elif serialization_type == 2:
            self.serializator_impl = yaml_serialize.YamlSerialize
        elif serialization_type == 3:
            self.serializator_impl = json_serialize.JSONSerialize

    def save_user(self, user):
        """common procedure to serialize by given type"""
        config = self.config_reader.read_config()
        path = config.get('Serialization', 'path')
        self.serializator_impl.save(user, path)

    def load_user(self):
        """common deserialize function"""
        config = self.config_reader.read_config()
        path = config.get('Serialization', 'path')
        return self.serializator_impl.load(path)
