#!/usr/bin/env python3

from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Invoice, InvoiceEntry, Item


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Item
        fields = "__all__"


class InvoiceEntrySerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = InvoiceEntry
        fields = "__all__"


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    # NOTE: related_name doesn't work :/, instead use <model_name>_set
    items = InvoiceEntrySerializer(many=True, source="invoiceentry_set")

    class Meta:
        model = Invoice
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    invoices = serializers.HyperlinkedIdentityField(
        many=True, view_name="invoice-detail", read_only=True
    )
    items = serializers.HyperlinkedIdentityField(many=True, view_name="item-detail")

    class Meta:
        model = User
        fields = ["id", "username", "invoices", "items"]
