from django.db import models
from django.conf import settings

# Create your models here.
class News(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=60)
    text = models.TextField()