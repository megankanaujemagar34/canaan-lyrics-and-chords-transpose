from django.contrib import admin

# Register your models here.
from .models import Song

@admin.register(Song)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title',)

    class Media:
        css={
            'all':('admin/css/custom.css',)
        }