# coding: utf-8

"""
FIXME
"""

import json
import time
from logging2 import Logger

logger = Logger('server')

CONFFILE = '/etc/overlord/a.json'

def _read_file():
    with open(CONFFILE) as cf:
        confdata = json.load(cf)
    return confdata

def _get_current_time() -> int:
    return int(time.time())


class StorageData:
    def __init__(self):
        self._start_time = _get_current_time()
        self._confdata = _read_file()

    def callback(self):
        current_time = _get_current_time()

        logger.info('current time={}, time of cache live={}, difference={}'.format(
            current_time,
            self._start_time,
            current_time - self._start_time
        ))

        if _get_current_time() - self._start_time > 10:
            logger.info('cache update!')
            self._confdata = _read_file()
            self._start_time = _get_current_time()
        return self._confdata
