# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-12 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import lib.orm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.IntegerField(verbose_name='好友id')),
                ('uid2', models.IntegerField(max_length=11, verbose_name='好友id')),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Swiped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=11, verbose_name='用户自身id')),
                ('sid', models.IntegerField(max_length=11, verbose_name='被滑的陌生人id')),
                ('mark', models.CharField(choices=[('喜欢', '喜欢'), ('超级喜欢', '超级喜欢'), ('不喜欢', '不喜欢'), ('反悔', '反悔')], max_length=32, verbose_name='滑动类型')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='会员名称')),
                ('level', models.IntegerField(max_length=32, verbose_name='登记')),
                ('price', models.FloatField(max_length=32, verbose_name='价格')),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
    ]