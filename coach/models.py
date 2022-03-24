from django.db import models


class Excel(models.Model):
    name = models.CharField(max_length=996)
    remark = models.CharField(max_length=1000, blank=True)
