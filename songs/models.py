from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    lyrics_and_chords = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title