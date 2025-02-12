"""This module handles logging for the script"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

current_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S")


def initialize_logger(log_path, file_name, logger_type):
    """
    This function will create an instance of a logger

    Args:
        log_path (str): Directory where to output the log file.
                        This path is indicated in the config file
        file_name (str): File name of the log file
        logger_type (str): Name of the logger to be called

    Returns:
        logger (logging.Logger): Returns the instance of the logger created
    """

    if not os.path.exists(log_path):
        os.makedirs(log_path, exist_ok=True)

    log_path = os.path.abspath(log_path)
    log_file = os.path.join(log_path, f"{file_name} - {current_time}.log")

    logger = logging.getLogger(logger_type)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_file, when="s", interval=5, backupCount=7)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
