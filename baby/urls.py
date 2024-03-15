from django.urls import path

from .views import index, details, book_list, community_view, book_detail

urlpatterns = [
    path("", index, name="home"),
    path("details/<int:pk>", details, name="details"),
    path("book-list/", book_list, name="book-list"),
    path("book-detail/<int:book_id>", book_detail, name="book-detail"),
    path("community/", community_view, name="community")
]
