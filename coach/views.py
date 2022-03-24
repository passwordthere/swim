from django.shortcuts import render
from rest_framework import viewsets
from . import serializers as s
from . import models as m


class ExcelViewSet(viewsets.ModelViewSet):
    queryset = m.Excel.objects.all().order_by('-id')
    serializer_class = s.ExcelSerializer
