# Django
网站设计

# 项目运行
    - Mac
    1. 启动redis（redis-server）
    2. 启动rabbitmq（rabbitmq-server）
    3. 运行celery（celery -A celery_tasks.tasks worker -l info）

## 主要模块
    - 登陆注册：实现非用户无法参与活动等条件(未完成！！！)
    - 主页（学校大全）：实现按照不同的分类进行排序
    - 分类页：
        - 基本信息页
        - 专业列表页
        - 历年分数页
        - 签约地区页
        - 签约单位页
        - 院校口碑页
        