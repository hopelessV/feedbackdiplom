from .forms import feedback
from .models import FeedbacksModel, User

from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from feedbac.settings import DEFAULT_FROM_EMAIL


def main_form(request):
    return render(request, 'start_window.html')

def consent(request):
    return render(request, 'includes/consent_window.html')

def feedback_detail(request, feedback_id):
    template = 'user/detail.html'
    detail = get_object_or_404(FeedbacksModel, pk=feedback_id)
    context = {
        'detail': detail,
    }
    return render(request, template, context)

def profile(request, username):
    template = 'user/profile.html'
    manager = get_object_or_404(User, username=username)
    page_obj = serializers.serialize('python',FeedbacksModel.objects.all())
    context = {
        'manager': manager,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def new_appeal(request):
    messages.warning(request, 'Вы согласны на обработку персональных данных')
    template = 'startform/feedback.html'
    appeal = FeedbacksModel
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
        # Это поле "Кому" (можно указать список адресов)
        ['to@example.com'],
        # Сообщать об ошибках («молчать ли об ошибках?»)
        fail_silently=True,
    )
    return render(request, template, context)
