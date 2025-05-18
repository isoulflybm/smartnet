from django.db import models
from django_enum import EnumField

# Create your models here.   

class City(models.Model):
    city = models.TextField(max_length=4095)
    
    def __str__(self): 
        return self.city
    
class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='+')
    street = models.TextField(max_length=4095)
    
    def __str__(self): 
        return f"{self.city}, {self.street}"

class Home(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='+')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='+')
    home = models.TextField(max_length=4095)
    
    def __str__(self): 
        return f"{self.street} {self.home}"

class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='+')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='+')
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='+')
    room = models.TextField(max_length=4095)
    floor = models.TextField(max_length=4095)
    entrance = models.TextField(max_length=4095)
    
    def __str__(self): 
        return f"{self.home}, {self.room}"

class TarifPayPeriod(models.TextChoices):
    SECOND = 'second', 'Second'
    MINUTE = 'minute', 'Minute'
    HOUR = 'hour', 'Hour'
    DAY = 'day', 'Day'
    MONTH = 'month', 'Month'
    
    class Meta:
        abstract = True

class Tarif(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, editable=False)
    deleted_at = models.DateTimeField(null=True, editable=False)
    name = models.TextField(max_length=4095)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    pay_period = EnumField(TarifPayPeriod, default=TarifPayPeriod.MONTH)
    
    def __str__(self): 
        return self.name

class Account(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, editable=False)
    deleted_at = models.DateTimeField(null=True, editable=False)
    name = models.TextField(max_length=4095)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='tarif')
    tarif_plan = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='tarif_plan')
    
    def __str__(self): 
        return f"{self.address}, {self.name}"
