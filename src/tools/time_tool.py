# coding: utf-8

"""
FIXME
"""

import functools
from datetime import datetime
from logging2 import Logger

logger = Logger('tools')

def time_difference(void):
    @functools.wraps(void)
    def wrapper(*args, **kwargs):
        time_elapsed = datetime.now().microsecond
        result = void(*args, **kwargs)
        logger.info('response time: {}ms'.format(datetime.now().microsecond - time_elapsed))
        return result
    return wrapper