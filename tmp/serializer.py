from rest_framework import serializers
from .models import *


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
