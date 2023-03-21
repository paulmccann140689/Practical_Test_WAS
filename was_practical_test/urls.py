
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from newsapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/', include('newsapp.urls')),
    path('admin/', admin.site.urls),
    ]