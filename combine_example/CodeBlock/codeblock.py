# !/usr/bin/env python
# -*- coding: utf-8 -*-


# 1. 根据 任务返回结果的 id 来查找对应任务的状态

# 创建一个任务
from cel.tasks import add
res = add.delay(3, 4)
>>>res.status
    'SUCCESS'
>>>res.id
    '432890aa-4f02-437d-aaca-1999b70efe8d'

# 重开一个 python shell
from celery.result import AsyncResult
from cel.tasks import app
res = AsyncResult(u'432890aa-4f02-437d-aaca-1999b70efe8d', app=app)
>>>res.state
    'SUCCESS'
>>>res.get()
    7


