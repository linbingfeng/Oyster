# -*- coding: utf-8 -*-
import redis
import os
from util import config_util

class RedisUtils():

    def __init__(self):
        redis_host = config_util.get_conf("REDIS_HOST")
        redis_port = int(config_util.get_conf("REDIS_PORT"))
        self.ex = None
        # self.ex = int(settings.CACHE_EX) * 60
        # self.ex = 5 * 60
        # redis_host = '192.168.9.66'
        # redis_port = 6379
        self.r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def put_price(self, hotel_id, check_in_date, channel_id, price):
        key = 'price_cache:%s_%s_%s' % (channel_id, hotel_id, check_in_date)
        self.r.set(key, price, ex= self.ex)

    def get_price(self,hotel_id, check_in_date, channel_id):
        key = 'price_cache:%s_%s_%s' % (channel_id, hotel_id, check_in_date)
        return self.r.get(key)

    def put_scenic_price(self, scenic_id, product_id, price):
        key = 'price_cache:%s_%s' % (scenic_id, product_id)
        self.r.set(key, price, ex=self.ex)

    def get_scenic_price(self,scenic_id, product_id):
        key = 'price_cache:%s_%s' % (scenic_id, product_id)
        return self.r.get(key)

    def put_scenic_product(self, scenic_id, product):
        key = 'product_cache:%s' % scenic_id
        self.r.set(key, product, ex=self.ex)

    def get_scenic_product(self, scenic_id):
        key = 'product_cache:%s' % scenic_id
        return self.r.get(key)

    def put(self, key, value, ex=None):
        if ex:
            self.r.set(key, value, ex=ex)
        else:
            self.r.set(key, value)

    def delete(self, key):
        self.r.delete(key)

    def get(self, key):
        return self.r.get(key)

    def hget(self, key, h_key):
        # key = 'productPrice:%s' % key
        return self.r.hget(key, h_key)

    def hset(self, key, h_key, value):
        # key = 'productPrice:%s' % key
        return self.r.hset(key, h_key, value)

if __name__ == '__main__':
    r = RedisUtils()
    print r.get_price('3418826','2016-08-13','1')