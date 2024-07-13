from django.urls import path

from customer.views.auth import LoginView, LogoutView, RegisterView
from customer.views.customers import CustomerListView, CustomerAddView, CustomerDeleteView, CustomerEditView, CustomerDetailView, export_data

urlpatterns = [
    path('customer-list/', CustomerListView.as_view(), name='customers'),
    path('customer-detail/<int:customer_id>', CustomerDetailView.as_view(), name='customer-detail'),
    path('add-customer/', CustomerAddView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('customer/<int:pk>/update', CustomerEditView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', LoginView.as_view(), name='login'),
    path('logout-page/', LogoutView.as_view(), name='logout'),
    path('register-page/', RegisterView.as_view(), name='register'),
    path('export-data/', export_data, name='export_data'),
]