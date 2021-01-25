#!/usr/bin/env python3

from django.urls import path, include
from .viewsets import InvoiceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("invoices", InvoiceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
