from django.shortcuts import render, redirect
from .assist import chatgpt
# Create your views here.

def home(request):
    try:
        if request.method == 'POST':
            response = chatgpt(request)
            context = response
            return render(request, 'assistant/home.html', context)
        else:
            return render(request, 'assistant/home.html')
    except:
        return redirect('error_handler')


def error_handler(request):
    return render(request, 'assistant/404.html')

