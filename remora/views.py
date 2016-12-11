from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    html = 'The current date and time is {:%d %b %Y %H:%m}'.format(datetime.datetime.now())
    return HttpResponse(html)

def plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    html = 'In {} hours it will be {:{time}}'.format(
        offset, now - datetime.timedelta(hours=offset), time='%H:%M')
    return HttpResponse(html)

