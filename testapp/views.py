from django.http import JsonResponse
from rest_framework import viewsets

from . import models as m
from . import serializers as s


class BookViewSet(viewsets.ModelViewSet):
    queryset = m.BookInfo.objects.all().order_by('-id')
    serializer_class = s.BookInfoSerializer
