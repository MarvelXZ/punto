from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import SupplierForm
from django.http import HttpResponse
from .forms import UploadPdfForm
from .models import Invoice, Supplier, ReceivedItem
import pdfplumber
import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InvoiceForm
from django.views.generic import DetailView


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'vendors/supplier_form.html'
    success_url = reverse_lazy('vendors:supplier_list')


class SupplierListView(ListView):
    model = Supplier
    template_name = 'vendors/supplier_list.html'
    context_object_name = 'suppliers'
    
    

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'vendors/invoice_detail.html'
    context_object_name = 'invoice'



def parse_luxol_invoice(file_path):
    products = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            products.extend(process_luxol_text(text))
    return products

def process_luxol_text(text):
    lines = text.split('\n')
    extracted_products = []
    for line in lines:
        match = re.search(r'(\w{12,})\s+(.*?)PZ\s+(\d+)\s+(\d+,\d+)\s+(\d+,\d+)', line)
        if match:
            vendor_code = match.group(1)
            naziv_artikla = match.group(2).strip()
            kolicina = int(match.group(3))
            cena_po_komadu = float(match.group(4).replace(',', '.'))
            ukupna_cena = float(match.group(5).replace(',', '.'))

            extracted_products.append({
                'Vendor Code': vendor_code,
                'Product Name': naziv_artikla,
                'Quantity': kolicina,
                'Unit Price': cena_po_komadu,
                'Total Price': ukupna_cena
            })

    return extracted_products



def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'vendors/invoice_list.html', {'invoices': invoices})


def invoice_add(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.total_amount = 0
            invoice.save()  
            
            if 'file' in request.FILES:
                file = request.FILES['file']

                with pdfplumber.open(file) as pdf:
                    products = []
                    for page in pdf.pages:
                        text = page.extract_text()
                        products.extend(process_luxol_text(text))

                total_amount = 0

                for product in products:
                    total_amount += product['Total Price']

                    ReceivedItem.objects.create(
                        invoice=invoice,
                        product_name=product['Product Name'],
                        vendor_code=product['Vendor Code'],
                        quantity=product['Quantity'],
                        unit_price=product['Unit Price'],
                        total_price=product['Total Price']
                    )
                invoice.total_amount = total_amount
                invoice.save()

            return redirect('vendors:invoice_list') 
        
    else:
        form = InvoiceForm()
    
    return render(request, 'vendors/invoice_add.html', {'form': form})
