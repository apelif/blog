# coding:utf-8
"""
一个博客
"""

from django.shortcuts import render_to_response, redirect
from blog.models import Article, User
from django.template import RequestContext
from blog.decorator import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def index(request):
    """首页
    """
    articles = article_paginator(request, 5)
    return render_to_response('index.html', {"articles": articles})

def detail(request, id):
    """文章页
    """
    article = Article.objects.get(id=str(id))
    return render_to_response('detail.html', {'article': article})

def login(request):
    """登录页
    """
    if request.session.get('username'):
        return redirect('/admin/')
    return render_to_response('login.html', RequestContext(request))

def login_verify(request):
    """登录验证
    """
    articles = article_paginator(request, 10)
    if request.session.get('username'):
        return render_to_response('admin.html', {"articles": articles})
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter(username=username)
    if user:
        if user.first().password == password:
            request.session['username'] = username
            return render_to_response('admin.html', {"articles": articles})
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')

@login_required
def article_del(request, id):
    """删除文章
    """
    article = Article.objects.get(id=str(id))
    article.delete()
    return redirect('/admin/')

@login_required
def article_new(request):
    """新建文章
    """
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    if not title or not content:
        return render_to_response('new.html',
                {'title': title, 'content': content})
    article = Article(title=title, content=content)
    article.save()
    return redirect('/admin/')

@login_required
def article_edit(request, id):
    """编辑文章
    """
    article = Article.objects.filter(id=str(id))
    title = article.first().title
    content = article.first().content
    title_mod = request.GET.get('title', '')
    content_mod = request.GET.get('content', '')
    if not title_mod or not content_mod:
        return render_to_response('edit.html',
                {'title': title, 'content': content})
    if title == title_mod and content == content_mod:
        return redirect('/admin/')
    if title == title_mod:
        article.update(content=content_mod)
        return redirect('/admin/')
    if content == content_mod:
        article.update(title=title_mod)
        return redirect('/admin/')
    article.update(title=title_mod, content=content_mod)
    return redirect('/admin/')

def article_paginator(request, page_num):
    """文章分页器
    """
    article_list = Article.objects.all()
    paginator = Paginator(article_list, page_num)
    page = request.GET.get('page', 1)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles
