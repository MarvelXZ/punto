from django.db import models
from django.utils.translation import gettext_lazy as _

class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    contact_person = models.CharField(max_length=255, verbose_name=_('Contact Person'), blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone Number'), blank=True, null=True)
    fax_number = models.CharField(max_length=20, verbose_name=_('Fax Number'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    website = models.URLField(verbose_name=_('Website'), blank=True, null=True)
    address = models.TextField(verbose_name=_('Address'), blank=True, null=True)
    registration_number = models.CharField(max_length=100, verbose_name=_('Registration Number'), blank=True, null=True)
    tax_code = models.CharField(max_length=100, verbose_name=_('Tax Code'), blank=True, null=True)
    vat_number = models.CharField(max_length=100, verbose_name=_('VAT Number'), blank=True, null=True)
    bank = models.CharField(max_length=255, verbose_name=_('Bank'), blank=True, null=True)
    bank_address = models.TextField(verbose_name=_('Bank Address'), blank=True, null=True)
    iban = models.CharField(max_length=100, verbose_name=_('IBAN'), blank=True, null=True)
    swift = models.CharField(max_length=100, verbose_name=_('SWIFT'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')



class Invoice(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='invoices', verbose_name=_('Supplier'))
    invoice_number = models.CharField(max_length=100, verbose_name=_('Invoice Number'))
    date = models.DateField(verbose_name=_('Invoice Date'))
    discount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Discount'), blank=True, null=True)
    fee_before_discount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Fee Before Discount'), blank=True, null=True)
    fee_after_discount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Fee After Discount'), blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Total Amount'))
    file = models.FileField(upload_to='invoices/', verbose_name=_('Invoice File'), blank=True, null=True)

    def __str__(self):
        return f"{self.invoice_number} - {self.supplier.name}"

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')



class ReceivedItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='received_items', verbose_name=_('Invoice'))
    vendor_code = models.CharField(max_length=100, verbose_name=_('Vendor Code'))
    product_name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Unit Price'))
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Total Price'))

    def __str__(self):
        return f"{self.product_name} - {self.invoice.invoice_number}"

    class Meta:
        verbose_name = _('Received Item')
        verbose_name_plural = _('Received Items')

