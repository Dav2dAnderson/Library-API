from django.urls import path

from .views import (CategoryListCreateAPIView, CategoryRetrieveDestroyAPIView, 
                    BookListCreateAPIView, BookRetrieveAPIView, 
                    BookByCategoryAPIView, AuthorListCreateAPIView, 
                    AuthorRetrieveUpdateDestroyAPIView, BookByAuthorAPIView)

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    # path('category/<slug:slug>/', CategoryRetrieveAPIView.as_view()),
    path('category/<slug:slug>/', CategoryRetrieveDestroyAPIView.as_view()),

    path('book/', BookListCreateAPIView.as_view()),
    path('book/<slug:slug>/', BookRetrieveAPIView.as_view()),
    path('book-by-category/<slug:category_slug>/', BookByCategoryAPIView.as_view()),
    path('book-by-author/<slug:author_slug>/', BookByAuthorAPIView.as_view()),

    path('author/', AuthorListCreateAPIView.as_view()),
    path('author/<slug:slug>/', AuthorRetrieveUpdateDestroyAPIView.as_view())
]