from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from jakubmeller.views import fp, aboutme, skills, history
#from jakubmeller.views import AddCVView

urlpatterns = [
    #general
    path('', fp, name='fp'),
    path('admin/', admin.site.urls),
    path('aboutme/', aboutme, name='aboutme'),
    path('skills/', skills, name='skills'),
    path('history/', history, name='history'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)