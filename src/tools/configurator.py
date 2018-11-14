# coding: utf-8

"""
FIXME
"""

import yaml

from logging2 import Logger

logger = Logger('main')

class ConfStorage:
    conf = {}

    def __init__(self):
        logger.info('read config file in module {}'.format(__name__))
        with open('../configs/main.yaml') as f:
            self.conf.update(yaml.load(f))
