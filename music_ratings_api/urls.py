from django.urls import path, include

from .views import (AlbumReviewDetail,
                    BandDetail,
                    BandList,
                    AlbumList,
                    AlbumDetail,
                    SongList,
                    AlbumReviewList,
                    AlbumReviewCommentList,
                    AlbumReviewCommentDetail,
                    AlbumReviewLikeList,
                    AlbumReviewLikeDetail)

urlpatterns = [
    path('bands', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),
    path('albums', AlbumList.as_view()),
    path('albums/<int:pk>', AlbumDetail.as_view()),
    path('songs', SongList.as_view()),
    path('reviews', AlbumReviewList.as_view()),
    path('reviews/<int:pk>', AlbumReviewDetail.as_view()),
    path('comments', AlbumReviewCommentList.as_view()),
    path('comments/<int:pk>', AlbumReviewCommentDetail.as_view()),
    path('likes', AlbumReviewLikeList.as_view()),
    path('likes/<int:pk>', AlbumReviewLikeDetail.as_view()),
]
