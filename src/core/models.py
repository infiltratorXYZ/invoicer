from django.db import models
from datetime import date


class Invoice(models.Model):
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
        ]
