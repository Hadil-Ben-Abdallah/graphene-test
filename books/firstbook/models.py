from django.db import models

class Book(models.Model):
  book_id = models.AutoField(primary_key=True)
  title = models.TextField()
  author = models.TextField()
