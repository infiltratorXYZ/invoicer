from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Invoice(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="invoices", on_delete=models.CASCADE
    )

    recipient = models.ForeignKey("InvoiceRecipient", on_delete=models.CASCADE)

    sequence_number = models.CharField(
        max_length=100, blank=True, unique=True, help_text="Invoice #"
    )

    invoice_date = models.DateField(default=date.today, help_text="Invoice date")
    due_date = models.DateField(blank=True, help_text="Due date")

    currency_label = models.CharField(
        max_length=5, help_text="Currency for the invoice eg. USD, EUR, $, €"
    )

    items = models.ManyToManyField(
        "Item", related_name="entries", through="InvoiceEntry"
    )

    # Other details
    notes = models.TextField(
        blank=True, help_text="Additional informations about invoice"
    )
    terms = models.TextField(
        "Terms & Conditions",
        blank=True,
        help_text="Additional informations about invoice",
    )

    class Meta:
        unique_together = [
            "sequence_number",
            "owner",
        ]


class InvoiceEntry(models.Model):
    """The name of the item, its quantity and price"""

    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    quantity = models.IntegerField("number of items", default=1)
    overwrite_unit_cost = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=2,
        help_text="Custom item price",
    )


class Item(models.Model):
    """Object/service to be sold"""

    owner = models.ForeignKey(
        "auth.User", related_name="items", on_delete=models.CASCADE
    )
    item_id = models.CharField(
        max_length=100, primary_key=True, unique=True, help_text="Item id"
    )
    name = models.CharField("Product name", max_length=100)
    unit_cost = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, help_text="Item price"
    )

    class Meta:
        unique_together = [
            "item_id",
            "name",
            "owner",
        ]


class CompanyDetails(models.Model):
    company_name = models.CharField(max_length=1024)

    # Address
    company_address = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    state = models.CharField(blank=True, max_length=1024)
    country = models.CharField(max_length=1024)
    zip = models.CharField(
        "ZIP / postal code", blank=True, max_length=12, help_text="ZIP / postal code"
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="Your name and last name"
    )
    company_details = models.ForeignKey(
        CompanyDetails, on_delete=models.CASCADE, help_text="Details of your company"
    )


class InvoiceRecipient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    bill_to = models.CharField(
        max_length=100, blank=True, null=True, help_text="Recipient full name"
    )

    client_company_details = models.ForeignKey(
        CompanyDetails,
        on_delete=models.CASCADE,
        help_text="Details of the client company",
    )
