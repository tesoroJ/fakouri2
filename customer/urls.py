from django.urls import path
from customer import views

urlpatterns = [
    path('', views.customers),
    path('<slug:slug>', views.customer),
]