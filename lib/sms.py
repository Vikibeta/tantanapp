import random

import requests
from django.core.cache import cache

from common.errors import VcodeExist
from worker import call_by_worker
from swiper import config


def gen_verify_code(length=6):
    '''产生验证码'''
    min_value = 10 ** (length - 1)
    max_value = 10 ** length
    number = random.randrange(min_value, max_value)
    return number


@call_by_worker
def send_sms(phonenum, msg):
    '''发送短信'''
    params = config.HY_SMS_PARAMS.copy()
    params['mobile'] = phonenum
    params['content'] = params['content'] % msg
    response = requests.post(config.HY_SMS_URL, data=params)
    return response


def send_verify_code(phonenum):
    '''发送验证码'''
    key = 'VCode-%s' % phonenum
    if not cache.has_key(key):
        vcode = gen_verify_code()
        send_sms(phonenum, vcode)
        cache.set(key, vcode, 300)
    else:
        raise VcodeExist


def check_vcode(phonenum, vcode):
    '''检查验证码'''
    cached_vcode = cache.get('VCode-%s' % phonenum)

    return cached_vcode == vcode
