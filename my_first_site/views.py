from django.http import HttpResponse
from django.shortcuts import render_to_response


def jodel(request):
    return render_to_response('index.html')

def hello(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
