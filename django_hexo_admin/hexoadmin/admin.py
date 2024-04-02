from django.contrib import admin

# Register your models here.


from .models import *


class hexo_config_admin(admin.ModelAdmin):
    model = hexo_config
    extra = 0
    list_display = ("id", "user", "config")
    pass

class hexo_theme_config_admin(admin.ModelAdmin):
    model = hexo_theme_config
    extra = 0
    list_display = ("id", "user","theme_title", "config")
    pass

class hexo_blog_md_admin(admin.ModelAdmin):
    model = hexo_blog_md
    list_display = ("id", "user", "title", "md_content")
    extra = 0
    pass

class hexo_theme_admin(admin.ModelAdmin):
    model = hexo_theme
    extra = 0
    list_display = ("id", "theme_name","theme_introduction", "theme_url","theme_preview_url", "theme_install_command")
    pass

admin.site.register(hexo_config, hexo_config_admin)
admin.site.register(hexo_theme, hexo_theme_admin)
admin.site.register(hexo_theme_config, hexo_theme_config_admin)
admin.site.register(hexo_blog_md, hexo_blog_md_admin)
