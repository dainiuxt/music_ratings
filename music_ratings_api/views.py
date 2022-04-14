from django.shortcuts import render
from rest_framework import generics, permissions
from .models import (Band,
                    Album,
                    Song,
                    AlbumReview,
                    AlbumReviewComment,
                    AlbumReviewLike)
from .serializers import (AlbumSerializer,
                        BandSerializer,
                        SongSerializer)
from rest_framework.exceptions import ValidationError

class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maby... ;)')

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        band = Band.objects.filter(pk=kwargs['pk'])
        if band.exists() and self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maby... ;)')

    def put(self, request, *args, **kwargs):
        band = Band.objects.filter(pk=kwargs['pk'])
        if band.exists() and self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maby... ;)')

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]