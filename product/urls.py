from django.urls import path

from . import views

urlpatterns = [
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name="product-edit"),
    path('add/', views.ProductCreateView.as_view(), name='product-add'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
    path('all/', views.ProductListView.as_view(), name="all-products"),
]
