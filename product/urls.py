from django.urls import path

from . import views

urlpatterns = [
    path('return/<int:pk>/', views.ProductInstanceReturnView.as_view(), name="product-return"),
    path('borrow/<int:pk>/', views.ProductInstanceBorrowView.as_view(), name="product-borrow"),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name="product-edit"),
    path('add/', views.ProductCreateView.as_view(), name="product-add"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
    path('all/', views.ProductListView.as_view(), name="all-products"),
]
