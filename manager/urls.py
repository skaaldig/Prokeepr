from django.urls import path

from . import views

urlpatterns = [
    path('rental-history/', views.RentalHistory.as_view(), name='rental-history'),
]
