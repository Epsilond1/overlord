# coding: utf-8

"""
FIXME
"""

import socket
import tornado.ioloop
import tornado.web

from cacher import Cacher
from configurator import ConfStorage
from logging2 import Logger
from time_tool import get_time_elapsed

logger = Logger('server')


def make_app():
    return tornado.web.Application([
        (r'/getConfig', Handler),
    ])

class Handler(tornado.web.RequestHandler):
    cacher = Cacher()
    cacher.reload_file()
    time_tocache = get_time_elapsed()
    cachettl = ConfStorage().conf.get('cachettl') # VERY BAD

    def get(self):
        if get_time_elapsed() - self.time_tocache < self.cachettl:
            self.write(self.cacher.get_cached_data())
        else:
            logger.info('cachemiss!')
            self.write(self.cacher.reload_file())
            self.time_tocache = get_time_elapsed()

class Server:
    def __init__(self, port):

        logger.info('try running server')

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = sock.connect_ex(('127.0.0.1', port))

        if not code:
            raise socket.error('port {} already used'.format(port))

        srv = make_app()
        srv.listen(port)

        logger.info('start listening port {}'.format(port))

        tornado.ioloop.IOLoop.current().start()
