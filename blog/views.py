# coding:utf-8

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from models import Article, User
from django.http import Http404
from django.template import RequestContext
from decorator import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render_to_response('index.html', {"articles": articles})

def detail(request, id):
    article = Article.objects.get(id=str(id))
    return render_to_response('detail.html', {'article': article})

def login(request):
    return render_to_response('login.html', RequestContext(request, locals())) 

def login_verify(request):
    articles = Article.objects.all()
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
    article = Article.objects.get(id=str(id))
    article.delete()
    return redirect('/admin/')

@login_required
def article_new(request):
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    if not title or not content:
        return render_to_response('new.html')
    article = Article(title=title, content=content)
    article.save()
    return redirect('/admin/')

@login_required
def article_edit(request, id):
    article = Article.objects.filter(id=str(id))
    title = article.first().title
    content = article.first().content
    title_mod = request.GET.get('title', '')
    content_mod = request.GET.get('content', '')
    if not title_mod or not content_mod:
        return render_to_response('edit.html',
                {'title': title, 'content': content})
    article.update(title=title_mod, content=content_mod)
    return redirect('/admin/')
