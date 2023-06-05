from django.shortcuts import render
from .forms import feedback
from .models import asd
from django.shortcuts import render, redirect

def main_form(request):
    return render(request, 'start_window.html')

def new_appeal(request):
    template = 'feedback.html'
    appeal = asd
    form = feedback(request.POST or None)
    context = {
        'appeal': appeal,
        'form': form,
    }
    if form.is_valid():
        form.save()
    return render(request, template, context)