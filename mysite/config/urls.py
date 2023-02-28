from django.contrib import admin
from django.urls import path, include
from todaysong import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todaysong/', include('todaysong.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index')
]
