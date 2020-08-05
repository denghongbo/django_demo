from django.db import models
from django.contrib.auth.models import User


class Procedure(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="UID")
    title = models.CharField(max_length=200)
    entity = models.BinaryField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

