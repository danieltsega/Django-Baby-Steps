from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Book
# Create your views here.

def index(request):
    articles = [
        {
            "id" : 1,
            "title": "Story of Tommy",
            "author": "Gusto Armeda",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/tommy.jpeg"
        },
        {
            "id" : 2,
            "title": "Grove Street Stories",
            "author": "Big Smoke",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/cj.jpeg"
        },
        {
            "id" : 3,
            "title": "Niko Bellic",
            "author": "Daniel Tsega",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/niko.jpeg"
        }
    ]
    return render(request, 'index.html', {'articles': articles})

def details(request, pk):
    articles = [
        {
            "id" : 1,
            "title": "Story of Tommy",
            "author": "Gusto Armeda",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/tommy.jpeg"
        },
        {
            "id" : 2,
            "title": "Grove Street Stories",
            "author": "Big Smoke",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/cj.jpeg"
        },
        {
            "id" : 3,
            "title": "Niko Bellic",
            "author": "Daniel Tsega",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/niko.jpeg"
        }
    ]
    article = next((article for article in articles if article['id'] == pk), None)
    return render(request, 'details.html', {"article": article})

#adding a logic to use database instead of local data
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {"books": books})

#adding book details page to filter db
def book_detail(request, book_id):
    book_item = Book.objects.filter(pk=book_id)
    return render(request, 'book_detail.html', {"book_item": book_item})

#adding a community page
def community_view(request):
    return render(request, 'community.html', {})