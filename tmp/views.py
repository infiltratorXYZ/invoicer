from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializer import *

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
