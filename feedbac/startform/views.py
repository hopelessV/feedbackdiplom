from django.shortcuts import render
from .forms import feedback
from .models import asd
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from feedbac.settings import DEFAULT_FROM_EMAIL

def main_form(request):
    return render(request, 'start_window.html')

def new_appeal(request):
    template = 'startform/feedback.html'
    appeal = asd
    form = feedback(request.POST or None)
    context = {
        'appeal': appeal,
        'form': form,
    }
    if form.is_valid():
        form.save()
    send_mail(
            'Тема письма',
            'Текст письма.',
            DEFAULT_FROM_EMAIL,  # Это поле "От кого"
            ['to@example.com'],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=True, # Сообщать об ошибках («молчать ли об ошибках?»)
        )
    return render(request, template, context)

def login_place(request):
    return render(request, 'user/login.html')