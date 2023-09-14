import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
import sys
from app.conf.config import *
from application import application

from tornado.options import define, options


define("port", default=8123, help="run on th given port", type=int)


def main():
    # 读取server的配置文件。
    conf_server = ServerConfig()
    options.port = int(conf_server.getPort())

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__" or 1 == 1:
    main()
