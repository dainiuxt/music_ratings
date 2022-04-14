from django.urls import path, include
from .views import BandDetail, BandList, AlbumList, SongList

urlpatterns = [
    path('bands', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),
    path('albums', AlbumList.as_view()),
    path('songs', SongList.as_view()),
]
