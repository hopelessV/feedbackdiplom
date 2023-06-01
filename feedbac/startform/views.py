from django.shortcuts import render
from feedbac.forms import feedback
from .models import asd
from django.shortcuts import get_object_or_404, render, redirect

def main_form(request):
    return render(request, 'start_window.html')

def new_appeal(request):
    template = 'feedback.html'
    appeal = get_object_or_404(asd)
    # if post.author != request.user:
    #     return redirect('posts:profile', username=post.author)
    form = feedback(request.POST or None, instance=appeal)
    context = {
        'appeal': appeal,
        'form': form,
    }
    form.save()
    return render(request, template, context)