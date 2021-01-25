from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True, help_text="Item id")
    name = models.CharField("Product name", max_length=100)
    rate = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Item price - unit cost"
    )

    class Meta:
        unique_together = [
            "id",
            "name",
            "user",
        ]


class Invoice(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sequence_number = models.IntegerField(help_text="Invoice #")
    sequence_number_prefix = models.CharField(
        max_length=5, blank=True, help_text="Prefix for invoice #"
    )

    invoice_date = models.DateField(default=date.today, help_text="Invoice date")
    due_date = models.DateField(default=date.today, help_text="Due date")

    currency_label = models.CharField(
        max_length=5, help_text="Currency for the invoice"
    )

    class Meta:
        unique_together = [
            "sequence_number_prefix",
            "sequence_number",
            "owner",
        ]
