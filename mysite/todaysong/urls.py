from django.urls import path
from todaysong import views 

app_name = 'todaysong'

urlpatterns = [
    path('', views.index, name='index'),
    path('song/send/', views.song_send, name='song_send'),
    path('song/receive/', views.song_receive, name='song_receive')
]
