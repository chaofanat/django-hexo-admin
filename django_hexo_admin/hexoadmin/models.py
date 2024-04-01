from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class apitest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class hexo_config(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    config = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def local_url(self):
        return self.user.username + str(self.id) + "hexoconfig.json"

    @property
    def key_config(self):
        return {
            "author": self.user.username,
            "url": "http://127.0.0.1:8081/blog/" + self.user.username,
            "root": "/blog/" + self.user.username + "/",
            "source_dir": "source/"
            + self.user.username
            + "_"
            + str(self.user.id)
            + "_source",
            "public_dir": "public/" + self.user.username,
            "tag_dir": "tags",
            "archive_dir": "archives",
            "category_dir": "categories",
            "new_post_name": ":title.md",
            "relative_link": "false",
        }


# author: ChaoFan #【用户名】
# url: http://127.0.0.1:8081/blog/chaofan
# root: /blog/chaofan/
# # Directory
# source_dir: source/chaofan_1_source

# public_dir: public/chaofan #【用户站点】

# tag_dir: tags
# archive_dir: archives
# category_dir: categories
# new_post_name: :title.md # 【File name of new posts】
# relative_link: false #【important】
# # Extensionshe
# ## Plugins: https://hexo.io/plugins/
# ## Themes: https://hexo.io/themes/
# theme: next
# theme_config:


class hexo_theme(models.Model):
    id = models.AutoField(primary_key=True)
    theme_name = models.CharField(max_length=255)
    theme_introduction = models.TextField(null=True)
    theme_url = models.CharField(max_length=255, null=True)
    theme_preview_url = models.CharField(max_length=255, null=True)
    theme_install_command = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class hexo_theme_config(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme_title = models.CharField(
        max_length=255, null=True, default="landscape"
    )  # 未与hexo_theme关联，但实际是hexo_theme的外键
    config = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class hexo_blog_md(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    md_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def local_url(self):
        return "source/" + self.user.username + "_" + str(self.user.id) + "_source"
