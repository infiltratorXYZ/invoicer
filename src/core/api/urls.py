#!/usr/bin/env python3

from django.urls import path, include
from .viewsets import InvoiceViewSet, UserViewSet, ItemViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("invoices", InvoiceViewSet)
router.register("users", UserViewSet)
router.register("items", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
