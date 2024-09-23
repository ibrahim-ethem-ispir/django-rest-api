import uuid
from django.db import models

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    stock = models.IntegerField()
    published = models.BooleanField()
    published_date = models.DateField()

    class Meta:
        db_table = 'book'
    