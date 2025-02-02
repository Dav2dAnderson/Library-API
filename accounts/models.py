from django.db import models
from django.contrib.auth.models import AbstractUser

from library.models import Book
# Create your models here.


class Customer(AbstractUser):
    downloaded_books = models.ManyToManyField(Book, related_name='downloaded_books', blank=True)
    enrolled_books = models.ManyToManyField(Book, related_name='enrolled_books', blank=True)

    def __str__(self):
        return self.username
    
