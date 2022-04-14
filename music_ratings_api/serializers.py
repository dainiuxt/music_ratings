from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['title']


class AlbumSerializer(serializers.ModelSerializer):
    # band = serializers.ReadOnlyField(source='band.title')
    # band_id = serializers.ReadOnlyField(source='band.id')

    class Meta:
        model = Album
        fields = ['band', 'title']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['album', 'title', 'duration', 'field_duration', 'status']