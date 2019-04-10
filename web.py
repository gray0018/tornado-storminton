#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.auth
import tornado.locale
from tornado import gen
from tornado.escape import json_encode, json_decode

from setting import settings
from setting import conn

from controller import auth
# from controller import home
# from controller import data
# from controller import pymail

from controller.base import WebRequest
import time

class MainHandler(WebRequest):
    @gen.coroutine
    def get(self, app):
        print self.current_user
        if not self.current_user:
            self.uri = self.request.uri
            self.render("template/404.html")
            return
        self.id = self.current_user["id"]
        self.render("template/home.html")




tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

application = tornado.web.Application([



    # (r"/api/email_code", pymail.EmailCodeAPIHandler),

    # (r"/api/login_weibo", auth.LoginWeiboAPIHandler),
    # (r"/api/login_wxapp", auth.LoginWxappAPIHandler),
    # (r"/api/login_gh", auth.LoginGhAPIHandler),
    (r"/api/login", auth.LoginAPIHandler),
    (r"/logout", auth.LogoutHandler),

    # (r"/home/(.*)", home.HomeHandler),
    # (r"/api/data/ws",data.DataWebSocket),
    (r"/(.*)", MainHandler),
    ],**settings)

if __name__ == "__main__":
    tornado.options.define("port", default=8001, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()
    application_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    application_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()