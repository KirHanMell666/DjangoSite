from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Article, Technology

@csrf_protect
def fp(request):
    return render(request, 'jakubmeller/fp.html')

@csrf_protect
def skills(request):
    technology = Technology.objects.all()
    return render(request, 'jakubmeller/skills.html', {'technologies': technology})

@csrf_protect
def aboutme(request):
    return render(request, 'jakubmeller/aboutme.html')

@csrf_protect
def history(request):
    return render(request, 'jakubmeller/history.html')
