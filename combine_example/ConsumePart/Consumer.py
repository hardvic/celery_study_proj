# !/usr/bin/env python
# -*- coding: utf-8 -*-

from combine_example.direct_tasks.tasks import add


class Consumer(object):
    """
    该类是消费类
    """

    def add_consumer(self, x=None, y=None):
        return add.delay(x, y)


if __name__ == '__main__':
    test = Consumer()
    re_list = []
    for i in xrange(10):
        re_list.append(test.add_consumer(i, i + 1))
    for each_re in re_list:
        print(each_re.id, each_re.state, each_re.get())

    from celery.result import AsyncResult
    from combine_example.celery_app import app

    # 根据对应的id 返回对应的结果.
    for each_re in re_list:
        res = AsyncResult(each_re, app=app)
        print(res.state, res.get(), )

