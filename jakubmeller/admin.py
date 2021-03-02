from django.contrib import admin

# Register your models here.

from .models import Article, Technology

admin.site.register(Article)
admin.site.register(Technology)

