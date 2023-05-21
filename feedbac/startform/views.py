from django.shortcuts import render

def main_form(request):
    return render(request, 'start_window.html')
