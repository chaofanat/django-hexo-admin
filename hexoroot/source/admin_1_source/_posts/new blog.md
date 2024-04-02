---
title: new blog
date: 2024-01-29 18:39:50
categories: tech
tags: django
id: 2
toc: true
---
# django项目部署
django项目部署的最流行的方法是linux系统下Nginx+uWSGI，这方面的教程是比较多的，部署也比较方便的，但是奈何作者不是一个正经程序员，用惯了windows，Linux再好，也懒得去学习。。。所以只能选择uWSGI的替代品waitress进行动态内容的处理。当然还有其他替代品可以使用。
在Windows系统下，如果你在寻找uWSGI的替代品，有几个选项可以考虑（ps:GPT-4:)：

1. **Daphne**: Daphne是一个HTTP, HTTP2和WebSocket协议服务器，为Django项目提供服务，尤其是在使用Channels时。虽然它主要是为了支持Django Channels设计的，但它也可以作为一个普通的ASGI服务器来运行其他Python web应用。

2. **Hypercorn**: Hypercorn支持HTTP/1, HTTP/2, 和WebSocket协议，并且能够运行任何ASGI兼容的Python应用。这包括由Django, FastAPI, 和Quart等框架构建的应用。Hypercorn是uWSGI和Gunicorn的一个现代替代品，特别适合于需要异步功能的应用。

3. **Waitress**: Waitress是一个纯Python编写的WSGI服务器，适用于Windows和其他操作系统。它被设计为全面兼容，并且能够承载各种类型的Python web应用。如果你的应用是基于WSGI的，而不是ASGI，Waitress是一个很好的选择。

4. **Gunicorn**: 虽然Gunicorn主要是为Unix系统设计的，但它也可以在Windows上通过WSL（Windows子系统Linux）运行。如果你的开发环境接近于生产环境（通常是Linux），使用WSL运行Gunicorn可能是一个不错的选择。

每个服务器都有其特点和最佳使用场景，所以选择哪一个取决于你的具体需求，比如你的应用是基于WSGI还是ASGI，你是否需要异步处理，以及你是否偏好纯Python解决方案等等。


##  django项目部署准备（当然项目必须先上传至服务器了）
1. 修改settings.py,将开发者模式关闭

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*'] #也可以设为服务器ip
```
2. settings.py设置STATIC_ROOT

```python
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
3. 项目url配置增加静态资源访问url，开发时用到静态资源的地方都应该早做准备

```python
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

4. cmd命令收集静态资源,这里可能会存在一些未知的问题，**建议收集后，将开发时指定的静态文件路径下的内容拷贝一份复制到static_root路径下，替换其自动收集的文件。**

```powershell
python manage.py collectstatic
```
PS:另外关于静态资源文件这里，对于项目上传至github，有一个小坑（某些方面也不算坑）：本地仓库的文件上传至GitHub后，空文件夹都消失了。。。。再加上相关代码没有处理好文件操作，出现了一些小问题。

5. 如果使用的mysql之类的非django自带的数据库，请在服务器上搭建好对应的环境，要能和settings.py里的数据库相关配置对应。
6. 别忘了项目依赖的包。在服务器上不建议使用虚拟环境，虽然不知道为什么，但是也的确没必要去新建一个环境，毕竟本地开发的时候的环境上传至github时是自动被忽略的。
7. 数据库环境准备好后，使用cmd进行项目数据库的建立。以及新建超级用户。

```powershell
python manage.py makemigrations
python manage.py migrate
```

```powershell
python manage.py createsuperuser
```
至此，django的部署准备就完成了
## waitress安装部署
waitress的安装部署应该是简单的不能再简单了，作者也没有去深究一些更细节的配置之类的，下面是一个最简单的能跑起来的方法。
1. 首先pip安装waitress

```powershell
pip install waitress
```
2. 在django项目下新建一个run.py文件

```python
#run.py
from waitress import serve
from ChaoFanOnline.wsgi import application

serve(
    app=application,
    host='127.0.0.1',
    port=8080
)
```
这样，waitress就部署完成，用python执行这个文件，waitress服务器就可以运行了

```powershell
python run.py
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7fc06684a53d4c19b374c293e1693d54.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/50e1b76a4e2a45beaf09b27b6f3fda15.png)

此时已经可以像django自带的runserver一样通过指定端口进行访问了，注意端口号不要设置为80和443.

## Nginx安装部署
1. 至官网下载[Nginx    ](https://nginx.org/en/download.html)https://nginx.org/en/download.html
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ddb9a2425fa74274b7cccc3de6ede55c.png)
2. 解压后，配置nginx-1.24.0\conf\nginx.conf文件，主要为以下两部分，一部分是动态部分的请求转发，一部分是静态文件请求的直接处理。其他的一些Nginx配置的相关内容不再赘述。

```xml
 location / {
            root   html;
            index  index.html index.htm;
            proxy_pass http://127.0.0.1:8080;#注意和waitress服务端口保持一致
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

#域名/static/与服务端的静态文件路径间的映射
#用于配置处理静态文件路径 /static/ 的请求的规则。在这里，使用 alias 指令指定静态文件的根目录。
location /static/ {
            alias ../staticfiles/;  # 将路径替换为你的静态文件路径（最后的斜杠不能少）根据nginx文件位置自行配置相对路径或者绝对路径。
        }
```

3. 使用cmd命令执行nginx.exe文件，开启nginx服务

```powershell
nginx.exe
```
4. 如果是在服务运行中修改的配置文件，需要重启服务

```powershell
nginx.exe -s reload
```
至此，nginx部署完毕，可通过127.0.0.1直接访问，域名绑定之类的，请自行配置。



## 结语
虽然并不算太复杂，但是摸索下来，也花了一个下午才完成，为什么一定要使用其他服务器替代django默认的服务器，django文档中有说明其自带的服务器并不安全与稳定，不适合生产环境部署，于是得使用Nginx等其他服务器进行替代，但是waitress的性能究竟如何，笔者尚未进行验证，或许后续会进行相关的测试。就本次实践而言，后续为异步服务器AWSGI也可以很方便的进行扩展。Daphne可能是个不错的选择，对于django特有的channels而言。
