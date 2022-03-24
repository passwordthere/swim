from . import models as m
from rest_framework import serializers


class BookInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.BookInfo
        fields = '__all__'
