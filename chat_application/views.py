# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import models
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout

def fetch_group(request):
    user = request.user.username
    try:
        m1 = models.group.objects.filter(user1=user)
        m2 = models.group.objects.filter(user2=user)
        contacts = {}
        for i in m1:
            model_id = str(i.model_id)
            contacts.update({model_id: i.user2})
        for i in m2:
            model_id = str(i.model_id)
            contacts.update({model_id: i.user1})
        return HttpResponse(json.dumps(contacts))
    except ObjectDoesNotExist:
        return HttpResponse(None)

def sign_out(request):
    logout(request)
    return render(request, 'index.html')

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('screen')
    else:
        e = 'Invalid Credentials'
        return render(request, 'index.html', {'e': e})

def sign_up(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    u = User.objects.filter(username=username)
    if u:
        e = 'Username Exists'
        return render(request, 'index.html', {'e': e})
    else:
        u = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
    login(request, u)
    return redirect('screen')

