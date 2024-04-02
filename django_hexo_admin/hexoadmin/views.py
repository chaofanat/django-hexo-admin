from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework import status

# Create your views here.

from .models import apitest
from rest_framework import viewsets
from .serializers import apitestSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json


class apitestViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = apitest.objects.all()
    serializer_class = apitestSerializer


from django.contrib.auth.models import User
from .serializers import UserSerializer


from django.contrib.auth.hashers import make_password


# 关闭csrf
@method_decorator(csrf_exempt, name="post")
class RegisterAPI(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 对密码进行加密
        password = request.data.get("password")
        encrypted_password = make_password(password)
        user = serializer.save(password=encrypted_password)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


from .serializers import (
    hexo_configSerializer,
    hexo_themeSerializer,
    hexo_theme_configSerializer,
    hexo_blog_mdSerializer,
)


from .models import (
    hexo_config,
    hexo_theme,
    hexo_theme_config,
    hexo_blog_md,
)

import json
from django.shortcuts import render, get_object_or_404


# 对于hexo_configSerializer只有获取或者修改两个api
@method_decorator(csrf_exempt, name="get")
@method_decorator(csrf_exempt, name="post")
class hexo_configAPI(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = hexo_config.objects.all()

    # 修改查询集，设置为当前用户
    def get_queryset(self):
        return hexo_config.objects.filter(user=self.request.user)

    serializer_class = hexo_configSerializer

    def get(self, request, *args, **kwargs):
        return self.u_retrieve(request, *args, **kwargs)

    # 缺失异常处理
    def post(self, request, *args, **kwargs):
        updateconfig = request.data.get("config")
        configobject = get_object_or_404(hexo_config, user=request.user)

        try:
            configobject.config = updateconfig
            configobject.save()
            jsonconfig = json.loads(configobject.config)
            key_config = configobject.key_config
            for k, v in key_config.items():
                jsonconfig[k] = v
            configobject.config = json.dumps(jsonconfig)
            configobject.save()
            return Response({"message": "success"})
        except Exception as e:
            return Response({"message": e})

    # 重写方法retrieve,使其在查询集为空的情况下创建对象并返回
    def u_retrieve(self, request, *args, **kwargs):
        """
        Retrieves the object,or create a new one.
        """

        queryset = self.get_queryset()
        if queryset:
            instance = queryset.first()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            config = {
                "title": "Hexo",
                "subtitle": "",
                "description": "",
                "keywords": "",
                "author": "John Doe",
                "language": "en",
                "timezone": "",
                "url": "http://example.com",
                "permalink": ":year/:month/:day/:title/",
                "permalink_defaults": "",
                "pretty_urls": {"trailing_index": "true", "trailing_html": "true"},
                "source_dir": "source",
                "public_dir": "public",
                "tag_dir": "tags",
                "archive_dir": "archives",
                "category_dir": "categories",
                "code_dir": "downloads/code",
                "i18n_dir": ":lang",
                "skip_render": "",
                "new_post_name": ":title.md",
                "default_layout": "post",
                "titlecase": "false",
                "external_link": {"enable": "true", "field": "site", "exclude": ""},
                "filename_case": 0,
                "render_drafts": "false",
                "post_asset_folder": "false",
                "relative_link": "false",
                "future": "true",
                "syntax_highlighter": "highlight.js",
                "highlight": {
                    "line_number": "true",
                    "auto_detect": "false",
                    "tab_replace": "",
                    "wrap": "true",
                    "hljs": "false",
                },
                "prismjs": {
                    "preprocess": "true",
                    "line_number": "true",
                    "tab_replace": "",
                },
                "index_generator": {"path": "", "per_page": 10, "order_by": "-date"},
                "default_category": "uncategorized",
                "category_map": "",
                "tag_map": "",
                "meta_generator": "true",
                "date_format": "YYYY-MM-DD",
                "time_format": "HH:mm:ss",
                "updated_option": "mtime",
                "per_page": 10,
                "pagination_dir": "page",
                "include": "",
                "exclude": "",
                "ignore": "",
                "theme": "landscape",
                "deploy": {"type": ""},
            }
            # 将congfig转为json字符串
            config_str = json.dumps(config)
            instance = self.get_queryset().model(
                user=self.request.user, config=config_str
            )
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)


@method_decorator(csrf_exempt, name="get")
class hexo_themeAPI(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = hexo_theme.objects.all()

    serializer_class = hexo_themeSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            self.get_serializer(self.get_queryset(), many=True).data,
            status=status.HTTP_200_OK,
        )


# 导入settings
from django.conf import settings
import os


@method_decorator(csrf_exempt, name="get")
class pull_hexo_themeAPI(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = hexo_theme.objects.all()

    serializer_class = hexo_themeSerializer

    def get(self, request, *args, **kwargs):
        theme_local_path = settings.HEXO_ROOT_URL + "/themes/"
        themes = os.listdir(theme_local_path)
        for theme in themes:
            if os.path.isdir(os.path.join(theme_local_path, theme)):
                if not self.queryset.filter(theme_name=theme).exists():
                    instance = self.queryset.model(theme_name=theme)
                    instance.save()

        return Response(
            self.get_serializer(self.get_queryset(), many=True).data,
            status=status.HTTP_200_OK,
        )


import yaml


@method_decorator(csrf_exempt, name="get")
@method_decorator(csrf_exempt, name="post")
class hexo_theme_configAPI(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = hexo_theme_config.objects.all()

    # 修改查询集，设置为当前用户
    def get_queryset(self):
        return hexo_theme_config.objects.filter(user=self.request.user)

    serializer_class = hexo_theme_configSerializer

    def get(self, request, *args, **kwargs):
        return self.u_retrieve(request, *args, **kwargs)

    # 缺失异常处理
    def post(self, request, *args, **kwargs):
        updateconfig = request.data.get("config")
        configobject = get_object_or_404(hexo_theme_config, user=request.user)
        configobject.config = updateconfig
        try:
            configobject.save()
            userhexoconfig = get_object_or_404(hexo_config, user=request.user)
            # 更新hexo_config,增加或者覆盖theme_config信息
            jsonconfig = json.loads(userhexoconfig.config)
            jsonconfig["theme_config"] = json.loads(updateconfig)
            jsonconfig["theme"] = configobject.theme_title
            # 将jsonconfig重新转为json字符串存回数据库
            userhexoconfig.config = json.dumps(jsonconfig)
            userhexoconfig.save()
            return Response({"message": "success"})
        except Exception as e:
            print(e)
            return Response({"message": "error"})

    # 重写方法retrieve,使其在查询集为空的情况下创建对象并返回
    def u_retrieve(self, request, *args, **kwargs):
        """
        Retrieves the object,or create a new one.
        """

        queryset = self.get_queryset()
        if queryset:
            instance = queryset.first()
            config = {}
            serializer = self.get_serializer(instance)
            theme_name = request.GET.get("theme_name", "")
            if not theme_name:
                return Response(serializer.data)
            if instance.theme_title == theme_name:
                return Response(serializer.data)
            else:
                theme_config_local_url = (
                    settings.HEXO_ROOT_URL + "/themes/" + theme_name + "/_config.yml"
                )
                if not os.path.exists(theme_config_local_url):
                    return Response(
                        {"message": "该主题未找到配置文件，请联系管理员修复主题文件"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                with open(theme_config_local_url, "r", encoding="utf-8") as f:
                    config = yaml.load(f, Loader=yaml.FullLoader)

                # 将congfig转为json字符串
                config_str = json.dumps(config)
                instance.config = config_str
                instance.theme_title = theme_name
                instance.save()
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
        else:
            config = {}
            theme_name = request.GET.get("theme_name", "")
            if not theme_name:
                return Response(
                    {"message": "未提供主题名称"}, status=status.HTTP_400_BAD_REQUEST
                )
            theme_config_local_url = (
                settings.HEXO_ROOT_URL + "/themes/" + theme_name + "/_config.yml"
            )
            if not os.path.exists(theme_config_local_url):
                return Response(
                    {"message": "该主题未找到配置文件，请联系管理员修复主题文件"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            with open(theme_config_local_url, "r", encoding="utf-8") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)

            # 将congfig转为json字符串
            config_str = json.dumps(config)
            instance = self.get_queryset().model(
                user=self.request.user, config=config_str, theme_title=theme_name
            )
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)


class bloglistAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = hexo_blog_md.objects.all()
    serializer_class = hexo_blog_mdSerializer

    def get_queryset(self):
        return hexo_blog_md.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )


import subprocess
import shutil

@method_decorator(csrf_exempt, name="put")
@method_decorator(csrf_exempt, name="post")
@method_decorator(csrf_exempt, name="delete")
class blogdetailAPI(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = hexo_blog_md.objects.all()
    serializer_class = hexo_blog_mdSerializer

    def get_queryset(self):
        return hexo_blog_md.objects.filter(user=self.request.user)

    # 新建blog
    def post(self, request, *args, **kwargs):
        data = request.data
        title = data["title"]
        md_content = data["md_content"]
        # 存入数据
        if self.get_queryset().filter(title=title).exists():
            return Response(
                {"message": "标题已存在"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            instance = self.get_queryset().model(
                user=self.request.user, title=title, md_content=md_content
            )
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    # 修改blog
    def put(self, request, *args, **kwargs):
        data = request.data
        id = data["id"]
        if not self.get_queryset().filter(id=id).exists():
            return Response({"message": "id不存在"}, status=status.HTTP_400_BAD_REQUEST)
        title = data["title"]
        md_content = data["md_content"]
        instance = self.get_queryset().get(id=id)

        # 清除hexo本地文件，如果存在的话
        baseurl = settings.HEXO_ROOT_URL
        bloglocalurl = baseurl + "/" + instance.local_url
        if os.path.exists(bloglocalurl):
            os.remove(bloglocalurl)

        # 更新数据
        instance = self.get_queryset().get(id=id)
        instance.title = title
        instance.md_content = md_content
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        data = request.data
        id = data["id"]
        if not self.get_queryset().filter(id=id).exists():
            return Response({"message": "id不存在"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            instance = self.get_queryset().get(id=id)
            baseurl = settings.HEXO_ROOT_URL
            bloglocalurl = baseurl + "/" + instance.local_url
            if os.path.exists(bloglocalurl):
                os.remove(bloglocalurl)
            instance.delete()
            return Response({"message": "删除成功"}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        id = request.GET.get("id")
        if not self.get_queryset().filter(id=id).exists():
            return Response({"message": "id不存在"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            baseurl = settings.HEXO_ROOT_URL
            instance = self.get_queryset().get(id=id)
            bloglocalurl = baseurl + "/" + instance.local_url
            dirs = bloglocalurl.replace("/" + instance.title + ".md", "")
            try:
                # 创建hexo博客本地文件路径以及写入文件
                if not os.path.exists(dirs):
                    os.makedirs(dirs)
                with open(bloglocalurl, "w", encoding="utf-8") as f:
                    f.write(instance.md_content)

                # 将userconfig写入本地文件
                userconfig = get_object_or_404(hexo_config, user=self.request.user)
                userconfiglocalurl = baseurl + "/" + userconfig.local_url
                userconfigcontent = userconfig.config
                with open(userconfiglocalurl, "w", encoding="utf-8") as f:
                    f.write(userconfigcontent)


                # 执行hexo generate命令，生成静态文件
                try:
                    subprocess.run(
                        ["hexo", "clean"],
                        text=True,
                        cwd=baseurl,
                        check=True,
                        shell=True,
                    )
                    subprocess.run(
                        ["hexo", "generate", "--config", userconfig.local_url],
                        text=True,
                        cwd=baseurl,
                        check=True,
                        shell=True,
                    )
                    dest_dir = settings.HEXO_SITE_URL+'/blog/'+instance.user.username
                    source_dir=baseurl+'/public/'+instance.user.username
                    if os.path.exists(dest_dir):
                        shutil.rmtree(dest_dir)
                    shutil.copytree(source_dir,dest_dir)
                except Exception as e:
                    print(e)
                    return Response(
                        {"message": "hexo generate失败，请检查hexo配置"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            except Exception as e:
                print(e)
                return Response(
                    {"message": "文件创建失败"}, status=status.HTTP_400_BAD_REQUEST
                )
