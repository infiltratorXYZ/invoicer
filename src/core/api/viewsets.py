#!/usr/bin/env python3

from core.models import Invoice
from .serializers import InvoiceSerializer
from rest_framework import viewsets


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
