from django.contrib import admin
from .models import UPS, Part, UPS_Part_quantity

# Register your models here.
admin.site.register(UPS)
admin.site.register(Part)
admin.site.register(UPS_Part_quantity)

