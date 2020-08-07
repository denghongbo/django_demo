from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    draft = models.BooleanField()

    def __str__(self):
        return self.title

