from .forms import feedback, PostForm, ResponseForm, ComentResponseForm
from .models import FeedbacksModel, User, Post

from django.http import HttpResponseRedirect
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
    form = ResponseForm(request.POST or None)
    context = {
        'detail': detail,
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

# def coment_feedback_detail(request, feedback_id):
#     template = 'feedback_post.html'
#     detail = get_object_or_404(Post, pk=feedback_id)
#     form = ComentResponseForm(request.POST or None)
#     context = {
#         'detail': detail,
#         'form': form,
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, template, context)

def all_posts(request):
    template = 'feedback_post.html'
    posts = Post.objects.all()
    page_obj = serializers.serialize('python',Post.objects.all())
    form = ComentResponseForm(request.POST or None)
    context = {
        'posts': posts,
        'page_obj': page_obj,
        'form': form,
    }
    if form.is_valid(): 
        my_model = Post.objects.get(pk=1)
        comment_response = form.save(commit=False)
        comment_response.response_status = 'some_status'
        comment_response.save(update_fields=['response_status'])
    return render(request, template, context)

def post_create(request):
    template = 'feed_post_create.html'
    create = Post
    form = PostForm(request.POST or None)
    context = {
        'create': create,
        'form': form
    }
    if form.is_valid():
        form.save()

        return redirect('appeal:main_form')
    return render(request, template, context)