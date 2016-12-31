import datetime
from django.http import Http404
from django.shortcuts import render
from remora.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def hello(request):
    return render(request, 'index.html', {'content': 'Hello there!'})

def current_datetime(request):
    content = 'The current date and time is {:%d %b %Y %H:%m}'.format(datetime.datetime.now())
    return render(request, 'cur_dt.html', {'content': content})

def plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    now = datetime.datetime.now()
    content = 'In {} hours it will be {:{time}}'.format(
        offset, now - datetime.timedelta(hours=offset), time='%H:%M')
    return render(request, 'plus.html', {'content': content})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'Nice Site!'})
    return render(request, 'contact_form.html', {'form': form})
