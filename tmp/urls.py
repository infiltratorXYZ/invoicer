from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "invoice_creator"

router = routers.DefaultRouter()
router.register(r"invoice", views.InvoiceViewSet)

urlpatterns = [
    path("", include(router.urls), name="api"),
]
