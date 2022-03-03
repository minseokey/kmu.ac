from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class shortURL(models.Model):
    path_word = models.CharField(max_length=200)
    url = models.TextField(null=False)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.path_word} {self.url}"
