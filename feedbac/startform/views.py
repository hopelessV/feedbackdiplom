from django.shortcuts import render
from .forms import feedback, test_feedback
from .models import asd, test
from django.shortcuts import get_object_or_404, render, redirect

def main_form(request):
    return render(request, 'start_window.html')

def new_appeal(request):
    template = 'feedback.html'
    appeal = asd
    # if post.author != request.user:
    #     return redirect('posts:profile', username=post.author)
    form = feedback(request.POST or None)
    context = {
        'appeal': appeal,
        'form': form,
    }
    if form.is_valid():
        form.save()
    return render(request, template, context)