from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name="omise_payment"),
    path('charge', views.charge, name="omise_charge"),
    path('webhook', views.webhook, name="omise_webhook")
]
