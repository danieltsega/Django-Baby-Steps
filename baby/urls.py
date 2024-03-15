from django.urls import path

from .views import index, details, book_list, community_view, book_detail, add_book, update_book, delete_book

urlpatterns = [
    path("", index, name="home"),
    path("details/<int:pk>", details, name="details"),
    path("book-list/", book_list, name="book-list"),
    path("book-detail/<int:book_id>", book_detail, name="book-detail"),
    path("community/", community_view, name="community"),
    path("add_book/", add_book, name="add-book"),
    path("update-book/<int:book_id>/", update_book, name="update-book"),
    path("delete-book/<int:book_id>/", delete_book, name="delete-book")
]
