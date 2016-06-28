from django.shortcuts import render
from settings import IS_DEVELOPMENT

# Create your views here.

def landing(request):
    context = {
        'DEVELOPMENT': IS_DEVELOPMENT,
    }
    return render(request, 'landing.html', context=context)
