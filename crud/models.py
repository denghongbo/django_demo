from django.db import models


class Demo(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Person(models.Model):
    """
    get_shirt_size_display()
    """
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)

    def __str__(self):
        return self.name


class Person2(models.Model):
    name = models.CharField("Person's name",
                            max_length=60,
                            help_text="Please input a name")
