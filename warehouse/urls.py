from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.WarehouseCreate.as_view(), name='warehouse-create'),
    path('update/<int:pk>/', views.WarehouseUpdate.as_view(), name='warehouse-update')
]
