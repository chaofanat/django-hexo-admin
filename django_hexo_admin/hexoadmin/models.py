from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings



#存储hexo配置文件(json)
class hexo_config(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    config = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def local_url(self):
        return self.user.username +'_'+ str(self.user.id) +'_'+ "hexoconfig.json"

    #指定关键配置，替换用户设定配置
    @property
    def key_config(self):
        url = settings.FOR_HEXOCONFIG_URL + "/blog/" + self.user.username

        return {
            "author": self.user.username,
            "url": url,
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

#存储hexo主题，需要管理员登录后台管理系统完成theme数据的登记，程序会自动拉取hexo根目录下的themes文件下的文件列表登记主题名称
class hexo_theme(models.Model):
    id = models.AutoField(primary_key=True)
    theme_name = models.CharField(max_length=255)
    theme_introduction = models.TextField(null=True)
    theme_url = models.CharField(max_length=255, null=True)
    theme_preview_url = models.CharField(max_length=255, null=True)
    theme_install_command = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#存储用户hexotheme配置，前端设置保存后，会自动添加到hexo_config中
class hexo_theme_config(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme_title = models.CharField(
        max_length=255, null=True, default="landscape"
    )  # 未与hexo_theme关联，但实际是hexo_theme的外键
    config = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#用户博客数据
class hexo_blog_md(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    md_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def local_url(self):
        return "source/" + self.user.username + "_" + str(self.user.id) + "_source"+"/_posts/"+self.title+".md"
