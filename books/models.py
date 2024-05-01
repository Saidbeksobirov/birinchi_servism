from django.db import models


class BookModel(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    info = models.TextField()
    pages = models.IntegerField()
    ebook = models.FileField(upload_to='media/ebooks', null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

