from rest_framework import serializers
from . import models as m


class ExcelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Excel
        fields = '__all__'
