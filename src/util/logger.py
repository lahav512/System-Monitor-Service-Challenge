import logging
import sys

logger = logging.getLogger(__name__)


def setup(log_level=logging.INFO):
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')

    file_handler = logging.FileHandler('errors.log')
    console_handler = logging.StreamHandler(sys.stdout)

    file_handler.setLevel(logging.WARNING)
    console_handler.setLevel(log_level)

    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.setLevel(log_level)
    return logger
