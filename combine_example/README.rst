该项目是个综合celery的项目

主要功能包括
1. tasks
    1.1 单任务
    1.2 chain a, b, c
    1.3 group 
    1.4 chord callback 
    1.5 map & starmap (fun1, fun2) -> (return[fun1], return[fun2])
    1.6 chunks for i in xrange(10000), 10 
    1.7 periodic tasks
    1.7.1   Entries
    1.7.2   crontab schedules
    1.7.3   starting the scheduler
    1.7.4   using custom scheduler classes
    1.7.5   running the worker as daemon 协程
    1.8 HTTP callback tasks
    
2. Workers
    2.1 启动, 停止, 重启 worker
    2.2 broadcast
    2.3 revoking tasks
    2.4 time limits
    2.5 rate limits
    2.6 running the worker as daemon
    
3. routing tasks (direct, *,#, fanout) 
4. Monitoring and management guide (flower)
5. security (白名单, [broker] redis, mysql, mongodb )
6. Configuration and defaults ()

7. 动态生成任务
8. 执行结果查询, 返回