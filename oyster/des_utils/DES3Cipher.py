# -*- coding: utf-8 -*-
import base64
import pyDes


class DES3Cipher:
    '''
    3DES加密解密
    '''
    def __init__(self, key='1234567812345678', iv='12345678'):
        self.key = key
        self.iv = iv


    def encrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.CBC, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        d = base64.encodestring(d)
        return d

    def decrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.CBC, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        data = base64.decodestring(data)
        d = k.decrypt(data)
        return d


if __name__ == '__main__':
    a = DES3Cipher('1234567812345678','12345678')
    data = 'hello world'
    data = a.encrypt(data)
    print data
    data = a.decrypt(data)
    print data