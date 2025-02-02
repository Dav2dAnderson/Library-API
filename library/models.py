from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        return super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Genre name")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Book(models.Model):
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=150, verbose_name="Title of book")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

    # class Meta:
    #     verbose_name_plural = "Books"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    



    