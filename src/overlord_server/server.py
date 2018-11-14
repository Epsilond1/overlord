# coding: utf-8

"""
FIXME
"""

import socket
import tornado.ioloop
import tornado.web

from storagedata import StorageData
from logging2 import Logger

logger = Logger('server')


def make_app():
    return tornado.web.Application([
        (r'/getConfig', Handler),
    ])

class Handler(tornado.web.RequestHandler):
    cacher = StorageData()

    def get(self):
        self.write(self.cacher.callback())

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
