from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ManufacuterCreate.as_view(), name='manufacturer-create'),
    path('update/<int:pk>/', views.ManufacturerUpdate.as_view(), name='manufacturer-update'),
    path('delete/<int:pk>/', views.ManufacturerDelete.as_view(), name='manufacturer-delete'),
    path('', views.ManufacturerList.as_view(), name='manufacturer-list')
]
