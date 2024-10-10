from django.contrib import admin
from django.urls import path, include
from . views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('vendors/', include('vendors.urls')),
    path('admin/', admin.site.urls),
]
