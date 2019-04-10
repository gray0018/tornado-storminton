#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

import logging
import uuid

from setting_info import apps_info, apps_arr, apps_host, baidu_ai_apps, baidu_fanyi_apps,city_json
from dev_type import dev_type_now

settings = {
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "demos_path": os.path.join(os.path.dirname(__file__),"demos"),
    "cookie_secret": "hotpoorinchina",
    "cookie_domain": "",
    "hotpoor_developers": [""],
    "QiniuAccessKey": "nyAmycfeo4-RF6drKPf62_KU1RUvj8lFsrmOqJ9K",
    "QiniuSecretKey": "NBaVPYokRuMvmthKWjabxFGCxQ0yx5h-ZSQwsJrk",
    "BaiduYuyinAppID": "9082071",
    "BaiduYuyinAPIKey": "PXirZpvwwZ9hsKqaLYcLXLzq",
    "BaiduYuyinSecretKey":"ef6788d39df2bb689437d0cb9b6dbda6",
    "debug": True,
    "wss_port":8001,
    "app": apps_info,
    "apps": apps_arr,
    "apps_host": apps_host,
    "BaiduAiApps":baidu_ai_apps,
    "dev_type":dev_type_now,
    "BaiduFanyiApps":baidu_fanyi_apps,
    "LoginCode":"hotpoor_simple_demo",
    "city_json":city_json,
    "developers":[]
}

try:
    import torndb as database
    conn = database.Connection("127.0.0.1:3306", "HTP", "root", "")
    conn1 = database.Connection("127.0.0.1:3306", "HTP1", "root", "")
    conn2 = database.Connection("127.0.0.1:3306", "HTP2", "root", "")
    
    ring = [conn1, conn2]
except:
    pass
