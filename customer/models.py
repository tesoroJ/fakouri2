from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.name)




class Customer_UPS(models.Model):
    brand = models.CharField(max_length=20)
    ups_model = models.CharField(max_length=20)
    power = models.CharField(max_length=10)
    serial_number = models.CharField(max_length=30)
    ups_date = models.DateField(default=None)
    battery_brand = models.CharField(max_length=20)
    battery_model = models.CharField(max_length=20)
    battery_string = models.IntegerField()
    battery_quantity = models.IntegerField()
    battery_date = models.DateField()
    input_cap_date = models.DateField()
    output_cap_date = models.DateField()
    dc_cap_date = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {}'.format(self.brand, self.ups_model, self.power, self.serial_number)
