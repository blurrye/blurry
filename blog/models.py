from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    # body = models.TextField()
    body = RichTextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # 文章摘要
    # excerpt = models.CharField(max_length=200, blank=True)
    excerpt = RichTextField()

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者,从 django.contrib.auth.models 导入
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title
