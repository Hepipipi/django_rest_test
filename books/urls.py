from django.urls import path
from books.views import HelloWorldAPIView, FavoriteMoviesAPIView, BookListAPIView, MovieAPIView, BookDeleteView
from books.views import (
    HelloWorldAPIView,
    FavoriteMoviesAPIView,
    BookListAPIView,
    MovieAPIView,
    BookDeleteView,
    ReviewListView,
    ReviewCreateView,
    ReviewDeleteView,
)
urlpatterns = [
    path('', HelloWorldAPIView.as_view(), name='hello-world'),
    path('fav_movies/', FavoriteMoviesAPIView.as_view(), name='fav_movies'),
    path('api/books/', BookListAPIView.as_view(), name='book-list'),
    path('api/movies/', MovieAPIView.as_view(), name='movie-list'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<book_id>/reviews/', ReviewListView.as_view(), name='reviews-list'),
    path('books/<book_id>/reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('books/<book_id>/reviews/<review_id>/delete/', ReviewDeleteView.as_view(), name='review-delete'),



]
