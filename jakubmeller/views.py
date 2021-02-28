from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Article

@csrf_protect
def fp(request):
    article = Article.objects.order_by("-date_added")[:4]
    return render(request, 'jakubmeller/fp.html', {'articles': article})
