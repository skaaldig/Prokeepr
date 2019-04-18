from django.urls import path

from . import views

urlpatterns = [

    path('return/<int:pk>/', views.ProductInstanceReturn.as_view(), name="product-return"),
    path('redirect/<int:pk>/', views.ProductInstanceRedirect.as_view(), name="return-redirect"),
    path('borrow/<int:pk>/', views.ProductInstanceBorrow.as_view(), name="product-borrow"),
    path('borrowed/', views.BorrowedProductList.as_view(), name="borrowed"),
    path('all/', views.ProductList.as_view(), name="all-products"),
]
