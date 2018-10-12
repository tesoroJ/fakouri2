from django.shortcuts import render
from .models import Customer, Customer_UPS
# Create your views here.


def customers(request):
    cust = Customer.objects.all().order_by('id')
    context = {
        'customers': cust,
    }
    return render(request, 'customer/templates/customers.html', context)


def customer(request, slug):
    ups = Customer.objects.get(name=slug)
    # cust = Customer_UPS.objects.all().get(customer_id=ups.id)
    cust = Customer_UPS.objects.filter(customer_id=ups.id)

    context = {
        'UPS': cust,
        'Customer': slug,
    }
    return render(request, 'customer/templates/customer.html', context)