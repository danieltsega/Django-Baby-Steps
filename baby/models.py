from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_cover/')
    
    def __str__(self):
        return self.title