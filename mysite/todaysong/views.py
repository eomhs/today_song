from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import date, timedelta
from .models import Song
from .forms import SongForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'todaysong/main_page.html')

@login_required(login_url='common:login')
def song_send(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.create_date = timezone.now()
            song.sender = request.user
            song.save()
            return redirect('todaysong:song_receive')
    else:
        form = SongForm()
    context = {'form':form}
    return render(request, 'todaysong/song_form.html', context)

def song_receive(request):
    today = date.today()
    yesterday = today - timedelta(days=1)
    song = Song.objects.filter(create_date=yesterday).exclude(sender=request.user, is_sent=True).order_by("?").first()
    if song is not None:
        song.is_sent = True
        song.save()
    context = {'song':song}
    return render(request, 'todaysong/song_receive.html', context)
