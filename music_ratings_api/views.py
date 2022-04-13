from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer

class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
