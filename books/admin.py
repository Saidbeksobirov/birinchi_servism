from django.contrib import admin
from books.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'pages', 'create_at']
    search_fields = ['title']
    list_filter = ['create_at', 'author']