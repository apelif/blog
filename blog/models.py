# coding:utf-8

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
