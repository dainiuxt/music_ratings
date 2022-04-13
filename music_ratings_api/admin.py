from django.contrib import admin
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
# Register your models here.

class SongInline(admin.TabularInline):
    model = Song
    extra = 0

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('band', 'title')
    inlines = [SongInline]

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0

class BandAdmin(admin.ModelAdmin):
  inlines = [AlbumInline]

admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)

