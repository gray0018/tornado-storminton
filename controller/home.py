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
import re
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
from nomagic.cache import get_user, get_users, update_user, get_doc, get_docs, update_doc, get_aim, get_aims, update_aim, get_entity, get_entities, update_entity
from nomagic.cache import BIG_CACHE
from setting import settings
from setting import conn

from base import WebRequest
from base import WebSocket

from wechat import weixin_access_token_for_apps
from wechat import weixin_JS_SDK_access_tokens
from wechat import weixin_JS_SDK_jsapi_tickets
from wechat import weixin_JS_SDK_access_token_timers
from wechat import WeixinJSSDKSign

# from weixin_jssdk import WeixinJSSDK

logger = logging.getLogger(__name__)

class HomeHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self,app):
        self.render("../template/home.html")
        
