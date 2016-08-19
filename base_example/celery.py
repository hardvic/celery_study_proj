# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery

# u'redis://:password@hostname:port/db_number'
BROKER_URL = u'redis://localhost:6379/0'

# u'redis://:password@hostname:port/db_number'
CELERY_RESULT_BACKEND = u'redis://localhost:6379/0'

app = Celery(main='celery_study_proj',
             backend=CELERY_RESULT_BACKEND,
             broker=BROKER_URL,
             include='base_example.tasks')

# Optional configuration, see the application user guide
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
