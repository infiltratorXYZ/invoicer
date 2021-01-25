#!/usr/bin/env python3

from rest_framework import serializers
from core.models import Invoice


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
