# -*- coding: utf-8 -*-
from __future__ import unicode_literals, HttpResponse, Http404, HttpResponseNotFound

from django.shortcuts import render

from datetime import datetime


# Create your views here.
def index(request):
    date = datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request, 'time_display/index.html', context) # updated this line
