from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response

from .models import (Band,
                    Album,
                    Song,
                    AlbumReview,
                    AlbumReviewComment,
                    AlbumReviewLike)

from .serializers import (AlbumSerializer,
                        BandSerializer,
                        SongSerializer,
                        AlbumReviewSerializer,
                        AlbumReviewCommentSerializer,
                        AlbumReviewLikeSerializer)

from rest_framework.exceptions import ValidationError

class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumSongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return Song.objects.filter(album=album)

class AlbumReviewList(generics.ListAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

class AlbumReviewCommentList(generics.ListAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer

class AlbumReviewLikeList(generics.ListAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        band = Band.objects.filter(pk=kwargs['pk'])
        if band.exists() and self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

    def put(self, request, *args, **kwargs):
        band = Band.objects.filter(pk=kwargs['pk'])
        if band.exists() and self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        album = Album.objects.filter(pk=kwargs['pk'])
        if album.exists() and self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

    def put(self, request, *args, **kwargs):
        album = Album.objects.filter(pk=kwargs['pk'])
        if album.exists() and self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumSongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return Song.objects.filter(album=album)

    def perform_create(self, serializer):
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(album=album)        

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        song = Song.objects.filter(pk=kwargs['pk'])
        if song.exists() and self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

    def put(self, request, *args, **kwargs):
        song = Song.objects.filter(pk=kwargs['pk'])
        if song.exists() and self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Became a superuser maybe... ;)')

# class AlbumReviewList(generics.ListCreateAPIView):
#     queryset = AlbumReview.objects.all()
#     serializer_class = AlbumReviewSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You can\'t touch this! ;)')

    def put(self, request, *args, **kwargs):
        review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('You can\'t touch this! ;)')

class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        review = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You can\'t touch this! ;)')

    def put(self, request, *args, **kwargs):
        review = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('You can\'t touch this! ;)')

class AlbumReviewLikeList(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(review=review, user = self.request.user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You can\'t touch this! ;)')        
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(review=review, user=self.request.user)  

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You can\'t touch this! ;)')

# class AlbumReviewLikeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AlbumReviewLike.objects.all()
#     serializer_class = AlbumReviewLikeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def delete(self, request, *args, **kwargs):
#         like = AlbumReviewLike.objects.filter(pk=kwargs['pk'], user=self.request.user)
#         if like.exists():
#             return self.destroy(request, *args, **kwargs)
#         else:
#             raise ValidationError('You can\'t touch this! ;)')

#     def put(self, request, *args, **kwargs):
#         like = AlbumReviewLike.objects.filter(pk=kwargs['pk'], user=self.request.user)
#         if like.exists():
#             return self.update(request, *args, **kwargs)
#         else:
#             raise ValidationError('You can\'t touch this! ;)')
