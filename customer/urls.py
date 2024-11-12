from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.customer_details, name='customer_details'),  
]

