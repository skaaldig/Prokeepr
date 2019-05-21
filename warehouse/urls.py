from django.urls import path

from . import views

urlpatterns = [
    path('create-manager/', views.WarehouseManagerCreate.as_view(), name='manager-create'),
    path('create/', views.WarehouseCreate.as_view(), name='warehouse-create'),
    path('update/<int:pk>/', views.WarehouseUpdate.as_view(), name='warehouse-update')
]
