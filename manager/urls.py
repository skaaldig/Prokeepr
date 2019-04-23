from django.urls import path

from . import views

urlpatterns = [
    path('update/<int:pk>/', views.ProductUpdate.as_view(), name='product-update'),
    path('new/', views.ProductCreate.as_view(), name='product-create')
]
