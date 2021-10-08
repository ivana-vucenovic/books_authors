from django.shortcuts import render
from .models import Author

def author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors.html', context)

