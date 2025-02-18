"""This module handles the config file and its parameters"""

import tomli


with open("./config/config.toml", "rb") as f:
    config = tomli.load(f)


def import_log_path():
    """Imports the log path from the config file"""

    log_path = config["path"]["log_path"]

    return log_path


def import_csv_output_path():
    """Imports the log path from the config file"""

    csv_path = config["path"]["csv_output_path"]

    return csv_path


def import_csv_input_path():
    """Imports the log path from the config file"""

    csv_input_path = config["path"]["csv_input_path"]

    return csv_input_path
