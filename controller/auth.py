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
        username = self.get_argument("username",None)
        password = self.get_argument("password",None)
        print username
        print password
        result = conn.query("SELECT COUNT(*) FROM member WHERE member_username = %s AND member_password = PASSWORD(%s)", username, password)
        print result
        if result[0]['COUNT(*)'] > 0:
            user_id = result[0].get("entity_id","")
            print result
            print u"=== 登录 ==="
            self.set_secure_cookie("user", tornado.escape.json_encode({"id": user_id, "v":1}),expires=time.time()+63072000,domain=settings.get("cookie_domain"))
            self.finish({"info":"success","login_account":login_account,"action":"redirect","redirect_uri":"/"})
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
