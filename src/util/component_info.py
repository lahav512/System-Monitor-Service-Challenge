import psutil
import random

from src.util.logger import logger


class Components:
    """
    Static class for PC components information
    """

    @staticmethod
    def get_mem():
        try:
            memory_info = psutil.virtual_memory()

            return {
                'usage': memory_info[2],
                'info': {
                    'Usage': f'{round(memory_info[3] / (1024 ** 3), 2)} GB',
                    'Available': f'{round(memory_info[1] / (1024 ** 3), 2)} GB',
                    'Total': f'{round(memory_info[0] / (1024 ** 3), 2)} GB',
                }
            }
        except Exception as e:
            logger.exception(e)
            return {}

    @staticmethod
    def get_cpu():
        try:
            cpu_info = (psutil.cpu_percent(interval=None),)

            return {
                'usage': cpu_info[0],
                'info': {
                    'Usage': f'{cpu_info[0]}%'
                }
            }
        except Exception as e:
            logger.exception(e)
            return {}

    @staticmethod
    def get_random():
        try:
            random_info = (random.randint(0, 100),)

            return {
                'usage': random_info[0],
                'info': {
                    'Usage': f'{random_info[0]}%'
                }
            }
        except Exception as e:
            logger.exception(e)
            return {}
