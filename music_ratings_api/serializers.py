from rest_framework import serializers
from django.contrib.auth.models import User
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
    album = serializers.ReadOnlyField(source='album.id')
    class Meta:
        model = Song
        fields = ['id', 'album', 'title', 'duration', 'status']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='review.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'review', 'comment_text']
        
class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    comment_count = serializers.SerializerMethodField()
    comments = AlbumReviewCommentSerializer(many=True)
    like_count = serializers.SerializerMethodField()
    # album = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'comments', 'ratings', 'comment_count',  'like_count']

    # def get_comments(self, review):
    #     return AlbumReviewComment.objects.filter(review=review).count()

    def get_comment_count(self, review):
        return AlbumReviewComment.objects.filter(review=review).count()

    def get_like_count(self, review):
        return AlbumReviewLike.objects.filter(review=review).count()

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='review.content')
    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'review']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
