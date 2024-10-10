from django.urls import path
from .views import SupplierCreateView, SupplierListView, invoice_add, invoice_list, InvoiceDetailView


app_name = 'vendors'

urlpatterns = [
    path('add/', SupplierCreateView.as_view(), name='supplier_add'),
    path('list/', SupplierListView.as_view(), name='supplier_list'),
    path('invoice/add/', invoice_add, name='invoice_add'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),


]
