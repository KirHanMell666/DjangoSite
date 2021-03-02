from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Article, Technology

@csrf_protect
def fp(request):
    technology = Technology.objects.all()
    return render(request, 'jakubmeller/fp.html', {'technologies': technology})
