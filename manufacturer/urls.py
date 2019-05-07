from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ManufacuterCreate.as_view(), name='manufacturer-create'),
    path('update/<int:pk>/', views.ManufacturerUpdate.as_view(), name='manufacturer-update')
]
