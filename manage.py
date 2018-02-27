#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/2/27 下午1:56
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : manage.py.py
# @Software: PyCharm
from admin import create_app
from config import current_config

__author__ = 'blackmatrix'

flask_app = create_app(current_config)


if __name__ == '__main__':
    pass
