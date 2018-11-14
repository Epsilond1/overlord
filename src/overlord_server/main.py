# coding: utf-8

"""
FIXME
"""

from server import Server
from configurator import ConfStorage

if __name__ == '__main__':
    _cfg_in_memory = ConfStorage()
    obj = Server(ConfStorage.conf.get('server_port')) # quickly start server
