# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from combine_example.celery_app import app
from celery import group

@app.task
def add(x, y):
    return x + y


@app.task
def pr_test(x, y):
    print('pr_test')
    return 'this is pr_test'


@app.task(bind=True)
def add_bind(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task()
def xsum(x):
    return sum(x)


# an example for AsyncResult.collect
@app.task(trail=True)
def A(how_many):
    return group(B.s(i) for i in range(how_many))()


@app.task(trail=True)
def B(i):
    return pow2.delay(i)


@app.task(trail=True)
def pow2(i):
    return i ** 2

