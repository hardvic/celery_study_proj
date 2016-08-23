# !/usr/bin/env python
# -*- coding: utf-8 -*-

from combine_example.direct_tasks.tasks import add, add_bind, mul, xsum
from combine_example.direct_tasks.tasks import A
from celery import chain, group, chord
from celery.result import ResultBase


class Consumer(object):
    """
    该类是消费类
    """

    def add_consumer(self, x=None, y=None):
        return add.delay(x, y)

    def add_bind_consumer(self):
        return add_bind.delay(x, y)

    def chain_consumer(self):
        return chain(add.s(3, 4), mul.s(6), mul.s(10)).apply_async()

    def group_consumer(self):
        return group(add.s(i, i) for i in range(10))().get()

    def chord_consumer(self):
        return chord((add.s(i, i) for i in range(10)), xsum.s())().get()

    def map_consumer(self):
        pass

    def starmap_consumer(self):
        pass

    def chunk_consumer(self):
        pass

    def periodic_consumer(self):
        pass

    def a_consumer(self, x):
        result = A.delay(x)
        # return list(result.collect())
        return [v for v in result.collect()
                if not isinstance(v, (ResultBase, tuple))]


if __name__ == '__main__':
    import time

    test = Consumer()
    print(test.group_consumer(), )
    print(test.chord_consumer(), )


    # chain 的实验
    # re = test.chain_consumer()
    # time.sleep(2)
    # print(re.ready(), )
    # print(re.successful(), )
    # print(re.get(), )





    # re_list = []
    # for i in xrange(10):
    #     re_list.append(test.add_consumer(i, i + 1))
    # for each_re in re_list:
    #     print(each_re.id, each_re.state, each_re.get())
    #
    # from celery.result import AsyncResult
    # from combine_example.celery_app import app
    #
    # # 根据对应的id 返回对应的结果.
    # for each_re in re_list:
    #     res = AsyncResult(each_re, app=app)
    #     print(res.state, res.get(), )

