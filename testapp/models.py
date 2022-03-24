from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=255)
    bpub_date = models.DateTimeField(max_length=255)
    bread = models.IntegerField(default=0)
    bcomment = models.CharField(max_length=255)
    # image = models.ImageField(max_length=255)
