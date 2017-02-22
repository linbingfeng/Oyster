# -*- coding: utf-8 -*-
import redis

class RedisUtils():

    def __init__(self,redis_host,redis_port=None,ex=None):
        if redis_port is None:
            redis_port = 6379
        self.ex = ex
        self.r = redis.StrictRedis(host=redis_host, port=int(redis_port), db=0)

    def put(self, key, value, ex=None):
        '''
        字符串
        :param key:
        :param value:
        :param ex:
        :return:
        '''
        if ex:
            self.r.set(key, value, ex=ex)
        else:
            self.r.set(key, value)

    def get(self, key):
        '''
        获取key对应的字符串
        :param key:
        :return:
        '''
        return self.r.get(key)

    def delete(self, key):
        '''
        删除redis中对应的key
        :param key:
        :return:
        '''
        self.r.delete(key)

    def hget(self, key, h_key):
        '''
        获取哈希表中的一个值
        :param key:
        :param h_key:
        :return:
        '''
        # key = 'productPrice:%s' % key
        return self.r.hget(key, h_key)

    def hset(self, key, h_key, value):
        '''
        设置哈希表中的一个值

        :param key:
        :param h_key:
        :param value:
        :return:
        '''
        # key = 'productPrice:%s' % key
        return self.r.hset(key, h_key, value)

    # 查询键（key中可包含匹配符）
    def check_key(self, key):
        return self.r.keys(key)

    # 自增
    def incr(self, key, default=1):
        # key = 'productNum:%s' % key
        if (1 == default):
            return self.r.incr(key)
        else:
            return self.r.incr(key, default)
    # 自减
    def decr(self, key, default=1):
        if (1 == default):
            return self.r.decr(key)
        else:
            return self.r.decr(key, default)

    def pop(self, key):
        return self.r.lpop(key)

    def push(self, key, value):
        self.r.lpush(key, value)

    def set_value(self, key, value,ex):
        self.r.set(name=key, value=value, ex=ex)

    def get_value(self, key):
        return self.r.get(key)

    def len(self, key):
        return self.r.llen(key)

    def get_all(self, key):
        k_len = self.r.llen(key)
        return self.r.lrange(key, 0, k_len)

    # def get(self, key):
    #     count  = self.r.get(key)
    #     if count is None:
    #         count = 0
    #     return int(count)
