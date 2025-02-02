from django.contrib import admin

from .models import Category, Book, Author
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname', ]
