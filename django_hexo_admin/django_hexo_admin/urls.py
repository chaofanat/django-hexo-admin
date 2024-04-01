"""
URL configuration for django_hexo_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# 导入include
from django.conf.urls import include
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

import posixpath
import mimetypes
from django.http import FileResponse, Http404, HttpResponse, HttpResponseNotModified
from django.utils.http import http_date, parse_http_date
from pathlib import Path
from django.utils._os import safe_join


def serve_index(request, path, document_root=None):

    path = posixpath.normpath(path).lstrip("/")
    path = "public/" + path
    fullpath = Path(safe_join(document_root, path))
    if fullpath.is_dir():
        fullpath = fullpath.joinpath("index.html")

    statobj = fullpath.stat()
    content_type, encoding = mimetypes.guess_type(str(fullpath))
    content_type = content_type or "application/octet-stream"
    response = FileResponse(fullpath.open("rb"), content_type=content_type)
    response.headers["Last-Modified"] = http_date(statobj.st_mtime)
    if encoding:
        response.headers["Content-Encoding"] = encoding
    return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hexoadmin/", include("hexoadmin.urls")),
    path("", RedirectView.as_view(url="hexoadmin/")),
    path("blog/<path:path>", serve_index, {"document_root": settings.HEXO_ROOT_URL}),
]
