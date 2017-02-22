#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

conf = {}

def get_conf(key,default=None):
    if not conf:
        with open(os.path.dirname(__file__) + '/conf/config.conf') as f:
            conf_str = f.readlines()
        for item in conf_str:
            if not item.startswith('#'):
                item_spilt = item.split('=')
                conf[item_spilt[0].strip()] = item_spilt[1].rstrip('\n').strip()
    return conf.get(key, default)