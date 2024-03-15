from django.urls import path

from .views import index, details, book_list

urlpatterns = [
    path("", index, name="home"),
    path("details/<int:pk>", details, name="details"),
    path("book-list/", book_list, name="book-list"),
]
