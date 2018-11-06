# coding: utf-8

"""
FIXME
"""

import socket
import tornado.ioloop
import tornado.web

from logging2 import Logger

logger = Logger('server')

def make_app():
    return tornado.web.Application([
        (r'/', Handler),
    ])

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.data_received(25)
        self.write('Hi, username...\nAccess allowed. Welcome!')


class Server:
    def __init__(self, configs):

        logger.info('try running server')

        application_port = configs.get('server_port')

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = sock.connect_ex(('127.0.0.1', application_port))

        if not code:
            raise socket.error('port {} already used'.format(application_port))

        srv = make_app()
        srv.listen(application_port)

        logger.info('start listening port {}'.format(application_port))

        tornado.ioloop.IOLoop.current().start()
