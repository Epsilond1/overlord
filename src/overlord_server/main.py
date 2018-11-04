# coding: utf-8

"""
FIXME
"""

import yaml

from server import Server
from str_tool import get_config_name
from logging2 import Logger

logger = Logger('main')

def load_configs() -> dict:
    logger.info('read config file in module {}'.format(__name__))

    config = {}
    with open(get_config_name(__name__)) as f:
        config.update(yaml.load(f))

    return config

if __name__ == '__main__':
    CONF_DICT = load_configs()
    obj = Server(CONF_DICT.get('server')) # quickly start server
