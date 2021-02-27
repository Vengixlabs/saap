from django.urls import path
from .views import ListSongsView , CreateSong , ExampleView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songup/', CreateSong.as_view(), name='song-upload'),
    path('songstats',ExampleView.as_view(), name='song-stats')
]