from django.db import models


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'Gold SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

