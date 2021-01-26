#!/usr/bin/env python3

from django.contrib.auth.models import User
from core.models import Invoice, Item, InvoiceEntry
from .serializers import (
    InvoiceSerializer,
    UserSerializer,
    ItemSerializer,
    InvoiceEntrySerializer,
)
from rest_framework import viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceEntryViewSet(viewsets.ModelViewSet):
    queryset = InvoiceEntry.objects.all()
    serializer_class = InvoiceEntrySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
