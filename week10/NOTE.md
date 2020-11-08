学习笔记
1. path, re_path
```python
# example
from django.urls import path, re_path
from . import view

urlpatterns = [
    path('douban', views.books_short),
    # 这里路径中的正则表单式会产生一个变量year，并将其传递给views.year_archive
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]
```
2. partial 
```python
from functools import partial
# int('str', base=10)
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
basetwo('10010')

# 注意事项
# 1 partial 第一个参数必须是可调用对象
# 2 参数传递顺序是从左到右，但不能超过原函数参数个数
# 3 关键字参数会覆盖partial中定义好的参数
```

3. include函数

4. 请求
```python
# HttpRequest由 WSGI 创建
# https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects
# 常见属性
# HttpRequest.scheme
# HttpRequest.method
# HttpRequest.encoding¶
# HttpRequest.GET , A dictionary-like object(QueryDict) containing all given HTTP GET parameters.
# HttpRequest.POST, A dictionary-like object(QueryDict) containing all given HTTP POST parameters, 
#     providing that the request contains form data. If you need to access raw or non-form data posted 
#     in the request, access this through the HttpRequest.body attribute instead
# HttpRequest.body, The raw HTTP request body as a bytestring. This is useful for processing data 
#     in different ways than conventional HTML forms: binary images, XML payload etc. For processing 
#     conventional form data, use HttpRequest.POST.
# HttpRequest.META
```

5. QueryDict
```python
# dict <-- MultiValueDict <-- QueryDict 
# 主要存储HTTP GET方法的请求参数
# http://127.0.0.1:8000/?id=1&id=2&name=wilson
# <QueryDict: {'id': ['1', '2'], 'name': ['wilson']}>
```
6. 响应
```python
# https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpResponse
# HttpResponse.content：响应内容
# HttpResponse.charset：响应内容的编码
# HttpResponse.status_code：响应的状态码
# HsonResponse 是HttpResponse 的子类，专门用来生成JSON 编码的响应。
```
7. Model
    ```python
    # 为什么自定义的Model要继承models.Model?
    # 不需要显式定义主键
    # 自动拥有查询管理器对象
    # 可以使用ORM API对数据库、表实现CRUD

    # 如何利用Manager(objects)实现对Model的CRUD？
    # 为什么查询管理器返回QuerySet对象？
    ```

    ```python
    # 如何让查询管理器的名称不叫做objects？
    from django.db import models
    from django.db.models import Manager

    class NewManager(Manager):
        pass

    class T1(models.Model):
        id = models.BigAutoField(primary_key=True)
        n_star = models.IntegerField()
        short = models.CharField(max_length=400)
        sentiment = models.FloatField()
        # 这里可以将原来的objects改为了object了
        object = NewManager()

        class Meta:
            managed = False
            db_table = 't1'
    ```

8. django管理页面
```python
# 将app的model添加都管理后台
# projectRootDir/appdir/admin.py
from django.contrib import admin
from . import models

admin.site.register(models.app_modelname)
```
9. Form ModelForm
```python
# 使用django的Form类创建表单对象
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)


# 使用model来创建表单
from django.forms import ModelForm
from myapp.models import Article
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']

# 表单与template, 通过变量form传递到template
# <form action="/login2" method="post">
#     {% csrf_token %}
#     {{ form }}
#     <input type="submit" value="Login">
# </form>
```

10. 登录与验证
```python
from django.contrib.auth import authenticate
from django.contrib.auth import login as ori_login
from django.contrib.auth import logout as ori_logout

# 验证成功,则返回一个auth.models.User对象
user = authenticate(username=username, password=password)

# 登录, 无论成功与否, 都不会返回数据
# doc https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/#login
ori_login(request, user)

# 退出登录, 无数据返回
# doc https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/#logout
ori_logout(request)
```

11. 信号
```python
# https://docs.djangoproject.com/zh-hans/2.2/ref/signals/
# 函数方式注册回调函数
from django.core.signals import request_started
request_started.connect(my_callback1)
# 装饰器方式注册回调函数
from django.core.signals import request_finished
from django.dispatch import receiver
@receiver(request_finished)
def my_callback2(sender, **kwargs):
    pass
```

12. 中间件
```python
# 中间件是全局改变输入或输出轻量级的、低级的“插件”系统对请求、响应处理的钩子框架
# example
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class Middle1(MiddlewareMixin):
    def process_request(self,request):
        print('中间件请求')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('中间件视图')
    def process_exception(self, request, exception):
        print('中间件异常')
    def process_response(self, request, response):
        print('中间件响应')return response
```

13. 生产环境部署
```python
pip install gunicorn

# 到项目root执行
gunicorn MyProject.wsgi

```
14. django 与 celery
  - Redis 安装和启动redis-server /path/to/redis.conf
  - Redis 安装和启动redis-server /path/to/redis.conf
        ```
        pip install celery
        pip install redis==2.10.6
        pip install celery-with-redis
        pip install django-celery
        ```
  - django 添加app
        ```
        django-admin startproject MyDjango
        python manager.py startapp djcron
        # 项目settings.py文件中添加app
        INSTALL_APPS=[
            # django-celery
            'djcelery',

            # 自建app
            'djcron', 
        ]
        ```

  - 迁移生成表
        ```
        python manage.py migrate
        ```

  - 配置django时区
        ```python
        # 以下5项是基本配置
        LANGUAGE_CODE = 'en-us'
        TIME_ZONE = 'UTC'
        USE_I18N = True
        USE_L10N = True
        USE_TZ = True
        
        # settings.py最后添加
        from celery.schedules import crontab
        from celery.schedules import timedelta
        import djcelery
        djcelery.setup_loader()
        BROKER_URL = 'redis://:123456@127.0.0.1:6379/'  # 代理人
        CELERY_IMPORTS = ('djcron.tasks')  # app
        CELERY_TIMEZONE = 'Asia/Shanghai'# 时区, 会覆盖django设置的时区
        CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' # 定时任务调度器
        ```
  - 在项目MyDjango下创建celery.py
        ```python
        import os
        from celery import Celery,platforms
        from django.conf import settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyDjango.settings')
        app = Celery('MyDjango')
        app.config_from_object('django.conf:settings')
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
        platforms.C_FORCE_ROOT = True
        
        @app.task(bind=True)
        def debug_task(self):
            print('Request: {0!r}'.format(self.request))
        ```
  - 在项目MyDjango的__init__.py添加
        ```python
        from __future__ import absolute_import # 文件第一行
        from .celery import app as celery_app
        ```

  - 在app下创建tasks.py
        ```python
        from MyDjango.celery import app

        
        @app.task()
        def get_task():
            return 'test'

        @app.task()
            def get_task2():
            return 'test2'
        ```

  - 启动Celery
        ```bash
        # 生产着
        Celerycelery -A MyDjango beat -l info

        # 消费者
        celery -A MyDjango worker -l info
        ```
  - 通过django admin管理页面增加定时任务

