from django.db import models

from lib.orm import ModelMixin


class Swiped(models.Model, ModelMixin):
    mark_type = (
        ('喜欢', '喜欢'),
        ('超级喜欢', '超级喜欢'),
        ('不喜欢', '不喜欢'),
        ('反悔', '反悔'),
    )
    uid = models.IntegerField(verbose_name='用户自身id')
    sid = models.IntegerField(verbose_name='被滑的陌生人id')
    mark = models.CharField(max_length=32, choices=mark_type, verbose_name='滑动类型')
    time = models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')


class Friend(models.Model, ModelMixin):
    uid1 = models.IntegerField(verbose_name='好友id')
    uid2 = models.IntegerField(verbose_name='好友id')


class Vip(models.Model, ModelMixin):
    name = models.CharField(max_length=32, verbose_name='会员名称')
    level = models.IntegerField(max_length=32, verbose_name='登记')
    price = models.FloatField(max_length=32, verbose_name='价格')


class Permission(models.Model, ModelMixin):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
