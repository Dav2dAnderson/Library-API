from django.shortcuts import render

from rest_framework import generics, permissions, filters
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .models import Category, Book, Author
from .serializers import CategorySerializer, BookSerializer, BookRetrieveSerializer, AuthorSerializer, AuthorRetrieveSerializer
# Create your views here.


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


"""APIViews for Category"""
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', ]
    search_fields = ['title', ]
    ordering_fields = ['title', ]
    permission_classes = [IsAdminOrReadOnly, ]


# class CategoryRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'


class CategoryRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]


"""APIViews for Book"""
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', ]
    search_fields = ['title', ]
    ordering_fields = ['title', ]
    permission_classes = [IsAdminOrReadOnly, ]


class BookByCategoryAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Book.objects.filter(category=category)
    

class BookByAuthorAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_slug = self.kwargs["author_slug"]
        author = get_object_or_404(Author, slug=author_slug)
        return Book.objects.filter(author=author)
    

class BookRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRetrieveSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fullname', ]
    ordering_fields = ['fullname', ]
    search_fields = ['fullname', ]
    permission_classes = [IsAdminOrReadOnly, ]


class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRetrieveSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]




