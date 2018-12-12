import os

from celery import Celery

from worker import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")


celery_app = Celery('swiper')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()


def call_by_worker(func):
    '''在 celery 中对任务进行异步调用'''
    task = celery_app.task(func)
    return task.delay
