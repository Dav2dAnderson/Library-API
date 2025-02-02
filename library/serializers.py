from rest_framework import serializers

from .models import Category, Book, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
 

class BookSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    author_fullname = serializers.CharField(source='author.fullname', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'category_title','author', 'author_fullname', 'price', 'image']


class BookRetrieveSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    author_fullname = serializers.CharField(source='author.fullname', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'category', 'category_title', 'author', 'author_fullname', 'price', 'image']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'fullname']
    

class AuthorRetrieveSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'fullname', 'bio', 'books']

    def get_books(self, obj):
        books = obj.books.all()
        return BookSerializer(books, many=True).data
    

