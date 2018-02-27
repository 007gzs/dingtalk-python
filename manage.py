#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/2/27 下午1:56
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : manage.py
# @Software: PyCharm
from admin import create_app
from admin.exts import manager
from config import current_config

__author__ = 'blackmatrix'

dingtalk_admin = create_app(current_config)


@manager.command
def devserver():
    dingtalk_admin.run(host=dingtalk_admin.config['HOST'], port=dingtalk_admin.config['PORT'])

if __name__ == '__main__':
    manager.run()
