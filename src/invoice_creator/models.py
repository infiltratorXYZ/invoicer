from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sequence_number = models.IntegerField(help_text="Invoice #")
    sequence_number_prefix = models.CharField(
        max_length=5, blank=True, help_text="Prefix for envoice #"
    )

    invoice_date = models.DateField(default=date.today, help_text="Invoice date")
    due_date = models.DateField(default=date.today, help_text="Due date")

    class Meta:
        unique_together = [
            "sequence_number_prefix",
            "sequence_number",
        ]
