# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    new_course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')

def remove_request(request, id):
    context = {
        'course_to_remove': Course.objects.get(id = id) 
    }
    return render(request, 'courses/remove.html', context)

def edit(request, id):
    context = {
        'user': User.objects.get(id = id) 
    }
    return render(request, 'users/edit.html', context)

def remove(request, id):
    course_delete = Course.objects.get(id = id).delete()
    return redirect('/')
