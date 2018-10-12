from django.db import models

# Create your models here.


class UPS (models.Model):
    brand = models.CharField(max_length=10)
    model_ups = models.CharField(max_length=10)
    power = models.CharField(max_length=10)

    def __str__(self):
        return '{} {} {} kVA'.format(self.brand, self.model_ups, self.power)


class Part(models.Model):
    type_part = models.CharField(max_length=10)
    part_number = models.CharField(max_length=20, default=None)
    values = models.CharField(max_length=20, default=None)
    description = models.CharField(max_length=30, default=None, blank=True)

    def __str__(self):
        return '{} {}'.format(self.part_number,self.type_part)


class UPS_Part_quantity(models.Model):
    ups = models.ForeignKey('UPS', on_delete=models.CASCADE, default=None)
    parts = models.ForeignKey('Part', on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=20, default=None, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '{} {} {} {}'.format(self.ups, self.parts.part_number, self.description, self.quantity)

