import configparser


class ConfigReader:

    def __init__(self, path=None):

        self.config = configparser.ConfigParser()
        if path is None:
            self.config.read("configs/config.ini")
            self.path = "configs/config.ini"
        else:
            self.config.read(path)
            self.path = path

    def read_config(self):
        return self.config

    def set_type(self, tp):
        if 0 < tp < 4:
            self.config.set('Serialization', 'type', str(tp))
        else:
            print("TYPE CAN BE 0< n <4")
