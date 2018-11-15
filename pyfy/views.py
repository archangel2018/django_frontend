from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import requests

class HomeView(TemplateView):
    template_name = 'index.html'

import ipdb


def ping(request):
    return HttpResponse('pong')

def msg(request):
    ipdb.set_trace()
    url = 'http: // backend2.geekyarun.com:8080 / demo / msg'
    r = requests.get('url')
    return HttpResponse(r.json())