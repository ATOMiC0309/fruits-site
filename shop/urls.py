from django.urls import path
from .views import index, all_product_by_category, product_detail

urlpatterns = [
    path('', index, name="index"),
    path('category/<str:category_slug>/', all_product_by_category, name="all_product_by_category"),
    path('product-detail/<int:pk>/', product_detail, name="product_detail"),
]