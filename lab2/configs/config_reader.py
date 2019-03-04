import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read("configs/config.ini")
    return config
