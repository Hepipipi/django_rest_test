from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book, Movie, Review
from books.serializers import BookSerializer, MovieSerializer, ReviewSerializer
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView
from django.core.exceptions import PermissionDenied


# Create your views here.
class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello world!'})


class FavoriteMoviesAPIView(APIView):
    movies = ["Inception", "The Matrix", "The Dark Knight"]

    def get(self, request):
        return Response({"movies": self.movies})

    def post(self, request):
        new_movie = request.data.get("movie")
        if new_movie:
            self.movies.append(new_movie)
            return Response({"message": "Movie added", "movies": self.movies})
        return Response({"error": "No movie provided"}, status=400)


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)  # many=True, т.к. список объектов
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from rest_framework.generics import DestroyAPIView

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Удаление доступно только администраторам.")
        instance.delete()


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book, Movie
from books.serializers import BookSerializer, MovieSerializer
from rest_framework.generics import UpdateAPIView
from django.core.exceptions import PermissionDenied


# Create your views here.
class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello world!'})


class FavoriteMoviesAPIView(APIView):
    movies = ["Inception", "The Matrix", "The Dark Knight"]

    def get(self, request):
        return Response({"movies": self.movies})

    def post(self, request):
        new_movie = request.data.get("movie")
        if new_movie:
            self.movies.append(new_movie)
            return Response({"message": "Movie added", "movies": self.movies})
        return Response({"error": "No movie provided"}, status=400)


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)  # many=True, т.к. список объектов
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from rest_framework.generics import DestroyAPIView

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Удаление доступно только администраторам.")
        instance.delete()


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book, Movie
from books.serializers import BookSerializer, MovieSerializer
from rest_framework.generics import UpdateAPIView
from django.core.exceptions import PermissionDenied


# Create your views here.
class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello world!'})


class FavoriteMoviesAPIView(APIView):
    movies = ["Inception", "The Matrix", "The Dark Knight"]

    def get(self, request):
        return Response({"movies": self.movies})

    def post(self, request):
        new_movie = request.data.get("movie")
        if new_movie:
            self.movies.append(new_movie)
            return Response({"message": "Movie added", "movies": self.movies})
        return Response({"error": "No movie provided"}, status=400)


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)  # many=True, т.к. список объектов
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from rest_framework.generics import DestroyAPIView

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDeleteView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
