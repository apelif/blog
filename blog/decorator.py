# coding:utf-8

from django.shortcuts import redirect

def login_required(func):
    def returned_wrapper(request, *args, **kwargs):
        if request.session.get('username'):
            return func(request, *args, **kwargs)
        return redirect('/login/')
    return returned_wrapper
