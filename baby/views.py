from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    articles = [
        {
            "title": "Story of Tommy",
            "author": "Gusto Armeda",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/tommy.jpeg"
        },
        {
            "title": "Grove Street Stories",
            "author": "Big Smoke",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/cj.jpeg"
        },
        {
            "title": "Niko Bellic",
            "author": "Daniel Tsega",
            "description": "The story begins in 1980 when miami was a place of drug lords and mafia centric and there was a god.......",
            "image" : "images/niko.jpeg"
        }
    ]
    return render(request, 'index.html', {'articles': articles})