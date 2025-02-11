"""This module handles the config file and its parameters"""

import tomli


def read_config_file():
    """Reads the config file"""

    with open("./config/config.toml", "rb") as f:
        config = tomli.load(f)

    return config


def import_log_path(config):
    """Imports the log path from the config file"""

    log_path = config["path"]["log_path"]

    return log_path
