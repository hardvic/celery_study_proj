# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from base_example.celery import app
import time

@app.task
def add(x, y):
    return x + y


@app.task
def add_sleep(x, y):
    time.sleep(30)
    return x + y


@app.task(ignore_result=True)
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)



