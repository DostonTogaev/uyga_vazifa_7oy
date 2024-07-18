from django.urls import path

from customer.views.auth import LoginView, LogoutView, register_page, LoginPage, verify_email_done,verify_email_confirm,verify_email_complete
from customer.views.customers import CustomerListView, CustomerAddView, CustomerDeleteView, CustomerEditView, CustomerDetailView, export_data, share_mail

urlpatterns = [
    path('customer-list/', CustomerListView.as_view(), name='customers'),
    path('customer-detail/<int:customer_id>', CustomerDetailView.as_view(), name='customer-detail'),
    path('add-customer/', CustomerAddView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('customer/<int:pk>/update', CustomerEditView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', LogoutView.as_view(), name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', export_data, name='export_data'),
    path('sending-mail/', share_mail, name='share_email'),
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
    path('verify-email-complete/', verify_email_complete, name='verify_email_complete'),
]