from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('clients', views.clients, name='clients'),
    path('invoices', views.invoices, name='invoices'),
    path('products', views.products, name='products'),
]