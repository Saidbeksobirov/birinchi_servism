from django.shortcuts import render

from books.models import BookModel


def books_list_view(request):
    books = BookModel.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)
