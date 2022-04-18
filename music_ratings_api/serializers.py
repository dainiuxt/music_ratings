from rest_framework import serializers
from .models import (Band,
                    Album,
                    Song,
                    AlbumReview,
                    AlbumReviewComment,
                    AlbumReviewLike)

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['title']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'band', 'title']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'album', 'title', 'duration', 'status']

class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    # album = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'album', 'content', 'ratings']

class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='review.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'review', 'content']

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'review']
