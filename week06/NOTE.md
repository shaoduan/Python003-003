学习笔记
1. orm 简单使用
```
# open interactive shell
python manage.py shell

# import your class which are defined in your app's models
from appName.models import tableName1, tableName2

# query all
tableName1.objects.all()

# create a record
row = tableName1(columnName1="xxxx", columnName2="yyyy")

# save record
row.save()
```

2. 逆向生成models
```
python manage.py inspectdb tablename
```

3. 修改模型流程
```
编辑 models.py 文件，改变模型。
运行 python manage.py makemigrations appname 为模型的改变生成迁移文件。
python manage.py sqlmigrate  appname 0001 查看做了哪些修改
运行 python manage.py migrate 来应用数据库迁移。
```

```
# tags and filters
# https://docs.djangoproject.com/zh-hans/2.2/ref/templates/builtins/#std:templatetag-comment
```

<h4>注释</h4>
```
<!-- 单行注释 -->
{# greeting #}

<!-- 多行注释 -->
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

#### 块与继承
```
{% extends "base.html" %}  # 声明继承哪个模板 

# 在父模板中声明可被子模板重写的块
{% block content %}{% endblock content %}

# 在子模板中复写
{% block content %}
    内容
{% endblock %}


```

#### url
```
# https://docs.djangoproject.com/zh-hans/2.2/ref/templates/builtins/#url
# Returns an absolute path reference (a URL without the domain name) matching a given 
# view and optional parameters. Any special characters in the resulting path will be
# encoded using iri_to_uri().
# This is a way to output links without violating the DRY principle by having to 
# hard-code URLs in your templates:

{% url 'some-url-name' v1 v2 %}

# The first argument is a URL pattern name. It can be a quoted literal or any other 
# context variable. Additional arguments are optional and should be space-separated 
# values that will be used as arguments in the URL. The example above shows passing 
# positional arguments. Alternatively you may use keyword syntax:

{% url 'some-url-name' arg1=v1 arg2=v2 %}

# If you'd like to retrieve a namespaced URL, specify the fully qualified name:

{% url 'myapp:view-name' %}
```

# url 示例
```
// https://docs.djangoproject.com/zh-hans/2.2/topics/http/urls/#url-namespaces-and-included-urlconfs


// in 'polls/urls.py' file
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]

// in urls.py file
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
]
```
