# celery_study_proj
celery demo

项目结构
--------
celery_study_proj
├── base_example
│   ├── celery.py
│   ├── celery.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── tasks.py
│   └── tasks.pyc
├── __init__.py
├── __init__.pyc
├── LICENSE
├── README.md
└── w1.log

一. Worker

1. 启动 worker
进入到 celery_study_proj 目录中, 启动 worker:

方式一： 直接启动

启动 worker
(test_env) liuquan@LiuQuan-Computer:~/pycharm_workspace/test/celery_study_proj$
  celery multi start -A base_example -l info
  
关闭 worker：
   直接 ctrl + c 或者 用 KILL 在终端杀死 

方式二： 在后台运行

启动 worker
(test_env) liuquan@LiuQuan-Computer:~/pycharm_workspace/test/celery_study_proj$
 celery multi start w1 -A base_example -l info
 其中 w1 是节点的意思, 可以设置多个节点

2. 重启 worker
celery multi restart w1 -A base_example -l info

3. 关闭 worker
关闭 worker 
不等待 worker 执行结束
celery multi stop w1 -A base_example -l info 

等待 worker 执行结束
celery multi stopwait w1 -A base_example -l info


二. Calling Task
1. 调用的三种方式 delay()  apply_async()   applying(__call__)
delay()
    传入对应的参数, 进行调用
>>> add.delay(2, 3)

apply_async()
    可以传入对应的可选参数
>>> add.apply_async((2, 2), queue='lopri', countdown=10)

applying(__call__)
    直接在当前的进程中执行调用, 不是异步的
>>> add(2, 4)

2. 返回结果
    delay() 和 apply_async() 返回 一个 AsyncResult 实例
    当设置了 result backend 时, 你可以根据该实例追踪这个任务的各种执行状态


>>>res = add.delay(2, 3)
获取执行结果 
>>>res.get(timeout=1)
判断执行状态
>>>res.failed()
True
>>>res.successful()
False

>>>res.state
'FAILURE'

3. 返回结果状态
PENDING -> STARTED -> SUCCESS

三. Canvas: Designing Workflows (需要配置对应的 backend)
1. subtask 
* subtask.apply_async(args=(), kwargs={}, **options)
* subtask.delay(*args, **kwargs)

2.Groups
group 通过并行的方式调用一组任务, 并且返回特殊的结果实例, 
你能通过这个结果实例看到返回的结果, 并且通过对应的顺序获取返回的结果.
>>> from celery import group
>>> from proj.tasks import add

>>> group(add.s(i, i) for i in xrange(10))().get()
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

部分group
>>> g = group(add.s(i) for i in xrange(10))
>>> g(10).get()
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

