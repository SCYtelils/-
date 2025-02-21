from django.http import HttpResponse
from django.shortcuts import render

import analyzer.tasks
import crawler.tasks
from analyzer import *


def index(request):
    return render(request, 'index.html')
