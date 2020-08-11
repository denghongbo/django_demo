from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    draft = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text
