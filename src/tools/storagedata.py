# coding: utf-8

"""
FIXME
"""

import json
from datetime import datetime
from time_tool import time_difference
from logging2 import Logger

logger = Logger('server')

CONFFILE = '/home/epsilond1/a.json'

def _read_file():
    with open(CONFFILE) as cf:
        confdata = json.load(cf)
    return confdata

def _get_current_time() -> int:
    return datetime.now().second

class StorageData:
    def __init__(self):
        self._start_time = _get_current_time()
        self._confdata = _read_file()

    def callback(self):
        if _get_current_time() - self._start_time > 10:
            logger.info('cache update!')
            self._confdata = _read_file()
            self._start_time = _get_current_time()
        return self._confdata
