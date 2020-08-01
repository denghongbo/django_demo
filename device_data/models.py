from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="UID")
    data_key = models.CharField(max_length=50, verbose_name="DATA_KEY")
    data_val = models.TextField(verbose_name="DATA_VALUE")

    def data_key_val(self):
        return "{},{}".format(self.data_key, self.data_val)

    data_key_val.short_description = u'Custom name'

    def __str__(self):
        return self.data_key
