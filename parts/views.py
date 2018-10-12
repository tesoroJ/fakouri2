from django.shortcuts import render, render_to_response
from .models import UPS, UPS_Part_quantity, Part

# Create your views here.


def eaton9315list(request):
    ups = UPS.objects.all()
    context = {
        'UPS': ups
    }
    return render(request,'parts/templates/9315capsandfans.html', context)


def eaton9315(request, slug):
    ups = UPS_Part_quantity.objects.filter(ups__power=slug)
    context = {
        'UPS': ups.order_by('parts__type_part'),
        'power': slug,
    }
    return render(request, 'parts/templates/Eaton_9315_parts.html', context)

