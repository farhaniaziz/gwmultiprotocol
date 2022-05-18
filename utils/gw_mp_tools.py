"""Tools file used for logging and useful methods for the project"""

__author__ = "Farhani Mouhamed Aziz, Aymen Majoul"
__license__ = "MIT"
__email__ = "farhaniaziz285@gmail.com, aimen.majoul@gmail.com"

import logging

GW_MP_LOG_FORMAT = '[%(asctime)s]::[%(levelname)s]::[GW_MP] %(message)s'

logging.basicConfig(level=logging.DEBUG, format=GW_MP_LOG_FORMAT)

def log_info(data):
    """Log with INFO level"""
    logging.info(data)

def log_debug(data):
    """Log with DEBUG level"""
    logging.debug(data)

def log_error(data):
    """Log with ERROR level"""
    logging.error(data)