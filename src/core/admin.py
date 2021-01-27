from django.contrib import admin
from .models import Invoice, Item, InvoiceEntry, InvoiceRecipient, CompanyDetails


class InvoiceEntries_inline(admin.TabularInline):
    model = InvoiceEntry
    extra = 3


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceEntries_inline,)


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item)
admin.site.register(InvoiceRecipient)
admin.site.register(CompanyDetails)
