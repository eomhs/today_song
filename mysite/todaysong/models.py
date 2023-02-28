from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    singer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name