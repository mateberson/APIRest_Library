from uuid import uuid4

from django.db import models

# Create your models here.

def uploadImageBook(instance, filename):
    return f'{instance.id_book}-{filename}'

class Books(models.Model):
    id_book=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    release_year=models.IntegerField()
    state=models.CharField(max_length=50)
    pages=models.IntegerField()
    publshing_company=models.CharField(max_length=255)
    create_at=models.DateField(auto_now_add=True) # auto_now_add adiciona data ao ser inserido no banco
    image=models.ImageField(upload_to=uploadImageBook, blank=True, null=True)
