from django.shortcuts import render,get_object_or_404
from .models import Song



# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html',{'songs':songs})

def song_detail(request, id ):
    song = get_object_or_404(Song, id=id)
    return render (request, 'songs/song_detail.html', {'song':song})

