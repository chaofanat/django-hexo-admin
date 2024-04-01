# Generated by Django 5.0.3 on 2024-03-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexoadmin', '0004_alter_hexo_theme_theme_install_command_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hexo_blog_md',
            name='md_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='hexo_blog_md',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hexo_theme_config',
            name='config',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='hexo_theme_config',
            name='theme_title',
            field=models.CharField(default='landscape', max_length=255, null=True),
        ),
    ]
