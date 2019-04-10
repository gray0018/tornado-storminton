# -*- coding: utf-8 -*-
import sys
import os
import os.path
import uuid
import time
import random
import string
import hashlib
import urllib
import copy
from functools import partial
import logging
import datetime

import tornado
import tornado.web
import tornado.escape
import tornado.websocket
import tornado.httpclient
import tornado.gen
from tornado.escape import json_encode, json_decode

# from user_agents import parse as uaparse #早年KJ用来判断设备使用

import nomagic
import nomagic.auth
from nomagic.cache import get_user, get_users, update_user, get_doc, get_docs, update_doc, get_aim, get_aims, update_aim, get_entity, get_entities, update_entity
from nomagic.cache import BIG_CACHE
from setting import settings
from setting import conn

from base import WebRequest
from base import WebSocket


logger = logging.getLogger(__name__)

class LoginAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def post(self):
        login_account = self.get_argument("login_account",None)
        result = conn.query("SELECT COUNT(*) FROM index_login WHERE login = %s ORDER BY id ASC", login_account)
        if result[0]['COUNT(*)'] > 0:
            print result
            print u"=== 登录 ==="
            self.finish({"login_account":login_account})
            return
        else:
            print u"=== 账号密码错误 ==="
            self.finish({"info":"reload"})
class LogoutHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        redirect_url = self.get_argument("next", "/")
        self.clear_cookie("user")
        self.clear_cookie('weibo_auth')
        self.clear_cookie('tab')
        self.redirect(redirect_url)
