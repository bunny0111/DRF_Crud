from django.urls import path, include
from expense import views

urlpatterns = [
    path('get-transactions/', views.get_transaction)
]
