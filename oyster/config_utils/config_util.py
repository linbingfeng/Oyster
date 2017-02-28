#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

conf = {}
path = '/conf/config.conf'

def get_conf(key,default=None):
    '''
    给定配置文件的位置，读取配置文件的内容
    :param key:
    :param default:
    :return:
    '''
    global path
    if not conf:
        with open(os.path.dirname(__file__) + path) as f:
            conf_str = f.readlines()
        for item in conf_str:
            if not item.startswith('#'):
                item_spilt = item.split('=')
                conf[item_spilt[0].strip()] = item_spilt[1].rstrip('\n').strip()
    return conf.get(key, default)

def set_conf_path(conf_path):
    '''
    日志文件路径需要在当前路径下
    :param conf_path:
    :return:
    '''
    global path
    path = conf_path