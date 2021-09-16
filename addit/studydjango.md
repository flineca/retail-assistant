# 注意点总结

## django 起步
### 创建项目
python中：在当前目录创建 web_project

    django-admin startproject web_project .

shell中查看版本：

    python -m django --version


### 创建app
一个Django project下可以有多个App，而一个App就是一个具体的Web应用程序，用来实现具体的功能和完成具体的事项。可以通过manage.py快速创建一个app：

    python manage.py startapp app1

### 在项目中启用app

在项目同名包的settings的INSTALLED_APPS 中添加设置

    'app1.apps.App1Config',

### 创建超级用户

    python manage.py createsuperuser

通过这个账户，可以快速使用 Django 强大的后台功能，对数据模型进行管理。我们可以运行项目，访问http://127.0.0.1:8000/admin路径登录



## Django中的Web开发

### 启动
通过django启动服务器端

    python manage.py runserver 127.0.0.1:8080

另外，其实python有内置的在当前目录启动服务器的方法

    python -m http.server 8080

### urls.py
django的app文件夹里要自己创建urls.py文件，内容像这样：

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

还要在项目根urls.py文件中插入新建的东西，让它看起来像这样：

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('app1/', include('app1.urls')),
        path('admin/', admin.site.urls),
    ]

注：admin.site.urls 不用include()？

### url(r'^index/$',views.index)是什么意思呢?

^匹配要检索的文本的开头,$匹配文本的结束，如http://127.0.0.1:port/index/

如果是url(r'^index/',views.index)，我们故意删除$，那么访问链接则可以在index/后面乱加字符串，依然能访问成功，比如http://127.0.0.1:port/index/sdfsdfsd

###  安全

任何使用POST表单的模板中，如果表单用于内部URL，请csrf_token在<form>元素中使用标记

对于以外部URL为目标的POST表单，不应这样做，因为这会导致CSRF令牌泄漏，从而导致漏洞。

### API开发
views.py中写函数，参数只需要request。
1. GET：会自动解析问号以前的路径
2. POST： 需要csrf。


## 数据库

### 命令行必要操作
同步数据库Django 1.7 及以上的版本需要用以下命令

    python manage.py makemigrations # 让django看看数据库有什么变化
    python manage.py migrate # 执行同步数据库

第一条命令是将你对models.py文件中的改动保存到当前目录中一个叫migrations的文件夹中，但还未同步到数据库

第二条命令将改动同步到数据库。

这两条命令在SQL等数据库中创建与models.py代码对应的表，不需要自己手动执行SQL

### 迁移的解释

django中内嵌了ORM框架，ORM框架可以将类和数据表进行对应起来，只需要通过类和对象就可以对数据表进行操作。ORM另外一个作用：根据设计的类生成数据库中的表。


### models.py编写时注意
给模型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django 自动生成的 admin 里也使用这个方法来表示对象。

- ？？？碰到没有objects的问题

写类的时候注意加上

    class Student(models.Model): 
        objects = models.Manager()

- time模块

一种查看最近修改的方法：

    import datetime
    from django.utils import timezone
        # ...
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

- ForeignKey: 多对一

参数需要加上

    on_delete=models.CASCADE

### 类与管理员后台接口

编辑 app1/admin.py 文件

    from .models import Class1
    admin.site.register(Class1)

## 前端

### 文件

自己在app1目录里创建一个 templates 目录，Django 将会在这个目录里查找模板文件。再创建一个目录app1，然后在其中新建一个文件 index.html 。换句话说，你的模板文件的路径应该是 app1/templates/app1/index.html 

虽然我们现在可以将模板文件直接放在 polls/templates 文件夹中（而不是再建立一个 polls 子文件夹），但是这样做不太好。Django 将会选择第一个匹配的模板文件，如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django 没有办法 区分 它们。我们需要帮助 Django 选择正确的模板，最好的方法就是把他们放入各自的 命名空间 中，也就是把这些模板放入一个和 自身 应用重名的子文件夹里。

### 去除模板中的硬编码

硬编码和强耦合的链接，对于一个包含很多应用的项目来说，修改起来是十分困难的。
然而，因为你在 app1.urls 的 url() 函数中通过 name 参数为 URL 定义了名字，你可以使用 {% url %} 标签代替它：

    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

如果你定义过path('<int:question_id>/', views.detail, name='detail'),那么这句的意思就是用question.id填入int:question_id的位置。

### 表单
action 为 {% url 'polls:vote' question.id %} 
使用 method="post"（与其相对的是 method="get"）是非常重要的，因为这个提交表单的行为会改变服务器端的数据。

### 重定向
重定向访问过程结束后，浏览器地址栏中显示的URL会发生改变，由初始的URL地址变成重定向的目标URL；请求转发过程结束后，浏览器地址栏保持初始的URL地址不变。

HttpResponseDirect。

redirect是URL重新定向的便捷方法，在django.shortcuts模块里。HttpResponseRedirect能支持的URL重定向，redirect都支持。redirect真正NB的地方在于，它不仅能根据URL重定向，还可以根据对象Object重定向和根据视图view重定向，根据视图重定向的时候还可以传递额外的参数。

reverse方法的作用是对已命名的URL进行反向解析，还传递相应的参数（args或带key的参数kargs)。该方法位于django.urls模块。reverse方法一般有2种应用场景:
- 在模型中自定义get_absolute_url时使用，传递参数
- 在视图中对命名URL进行解析，传递参数，再使用HttpResponseDirect和redict进行重定向


### 通用视图
ListView 和 DetailView 。
这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。

每个通用视图需要知道它将作用于哪个模型。 这由 model 属性提供。

DetailView 期望从 URL 中捕获名为 "pk" 的主键值，所以我们为通用视图把 question_id 改成 pk 。默认情况下，通用视图 DetailView 使用一个叫做 <app name>/<model name>_detail.html 的模板。在我们的例子中，它将使用 "polls/question_detail.html" 模板。template_name 属性是用来告诉 Django 使用一个指定的模板名字，而不是自动生成的默认名字。 我们也为 results 列表视图指定了 template_name —— 这确保 results 视图和 detail 视图在渲染时具有不同的外观，即使它们在后台都是同一个 DetailView。

类似地，ListView 使用一个叫做 <app name>/<model name>_list.html 的默认模板；我们使用 template_name 来告诉 ListView 使用我们创建的已经存在的 "polls/index.html" 模板。

：：：所以，如果使用ListView，则需要
1. 写class XxxxxxListView(ListView)指定各种参数如model，paginate_by，template_name。。。
2. 写class XxxxxxListView(ListView)编写规定范围内的几个方法（看文档），如get_queryset()
2. 在app/urls.py里改path('', XxxxxxxListView.as_view(), name='xxxx')这种形式
3. html文件中变量名要和ListView带的方法所规定的名字对应



## 测试

### 测试驱动
一些开发者遵循 "测试驱动" 的开发原则，他们在写代码之前先写测试。这种方法看起来有点反直觉，但事实上，这和大多数人日常的做法是相吻合的。我们会先描述一个问题，然后写代码来解决它。「测试驱动」的开发方法只是将问题的描述抽象为了 Python 的测试样例。

### 使用shell

    python manage.py shell

### 创建测试

Django 应用的测试应该写在应用的 tests.py 文件里。我们可以创建一个 django.test.TestCase 的子类，并添加方法。
    
    import datetime
    from django.test import TestCase
    from django.utils import timezone
    from .models import Question
    
    class QuestionModelTests(TestCase):
        def test_was_published_recently_with_future_question(self):
            """
            was_published_recently() returns False for questions whose pub_date
            is in the future.
            """

### 运行测试
测试系统会自动的在所有以 tests 开头的文件里寻找并执行测试代码。

    python manage.py test app1

以下是自动化测试的运行过程：

- python manage.py test polls 将会寻找 polls 应用里的测试代码
- 它找到了 django.test.TestCase 的一个子类
- 它创建一个特殊的数据库供测试使用
- 它在类中寻找测试方法——以 test 开头的方法。
- 在 test_was_published_recently_with_future_question 方法中，它创建了一个 pub_date 值为 30 天后的 Question 实例。
- 接着使用 assertls() 方法，发现 was_published_recently() 返回了 True，而我们期望它返回 False。

### client
    $ python manage.py shell
    >>> from django.test.utils import setup_test_environment
    >>> setup_test_environment()
    >>> from django.test import Client
    >>> client = Client()


## 其他
### MTV
> Django的MTV模式本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同，Django的MTV分别代表：  
- Model(模型)：负责业务对象与数据库的对象(ORM)
- Template(模版)：负责如何把页面展示给用户
- View(视图)：负责业务逻辑，并在适当的时候调用Model和Template  
> 此外，Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template