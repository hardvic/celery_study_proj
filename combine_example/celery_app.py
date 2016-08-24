# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery


BROKER_URL = u'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = u'redis://localhost:6379/0'

app = Celery(main='celery_study_proj',
             backend=CELERY_RESULT_BACKEND,
             broker=BROKER_URL,
             include='combine_example.direct_tasks.tasks')

app.conf.CELERY_TIMEZONE = 'Asia/Shanghai'

if __name__ == '__main__':
    app.start()

