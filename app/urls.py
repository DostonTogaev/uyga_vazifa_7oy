from django.contrib import admin
from django.urls import path, include
from app.views import ProductListView, ProductDetailView, AddProductView, EditProductTemplateView, DeleteProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product-detail/<int:product_id>', ProductDetailView.as_view(), name='product_detail'),

    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('edit-product/<int:pk>/', EditProductTemplateView.as_view(), name='edit_product'),
    path('delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
]
