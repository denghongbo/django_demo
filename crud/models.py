from django.db import models


class Demo(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.username

