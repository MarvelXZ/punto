from django import forms
from .models import Supplier, Invoice

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'contact_person',
            'phone_number',
            'address',
            'email',
            'website',
            'fax_number',
            'registration_number',
            'tax_code',
            'vat_number',
            'bank',
            'iban',
            'swift',
            ]

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class UploadPdfForm(forms.Form):
    pdf_file = forms.FileField(label='Select a PDF')
    



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'supplier',
            'invoice_number',
            'date',
            'discount',
            'fee_before_discount',
            'fee_after_discount',
            'file',
            ]
