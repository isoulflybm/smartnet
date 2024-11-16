from django.db import models

# Create your models here.

class TarifPeriod(models.TextChoices):
    SECONDS = 'SECONDS', 'seconds'
    MINUTES = 'MINUTES', 'minutes'
    HOURS = 'HOURS', 'hours'
    DAYS = 'DAYS', 'days'
    WEEKS = 'WEEKS', 'weeks'
    MONTHS = 'MONTHS', 'months'
    YEARS = 'YEARS', 'years'

class Tarif(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 32768)
    price = models.IntegerField()
    period = models.CharField(
        choices = TarifPeriod.choices, max_length = 256, default = TarifPeriod.MONTHS
    )
    count = models.IntegerField()

class Firewall(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 32768)
    ip = models.CharField(max_length = 256)
    tarif = models.ForeignKey(Tarif, on_delete = models.CASCADE, default = False)

class IpType(models.TextChoices):
    IP = 'IP', 'ip'
    NET = 'NET', 'net'

class IpArea(models.TextChoices):
    IP4 = 'IP4', 'ip4'
    IP6 = 'IP6', 'ip6'

class FirewallRestriction(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 32768)
    firewall = models.ForeignKey(Firewall, on_delete = models.CASCADE, default = False)
    ip_type = models.CharField(max_length = 256, choices = IpType.choices, default = IpType.IP)
    ip_area = models.CharField(max_length = 1024, choices = IpArea.choices, default = IpArea.IP4)
    ip_destination = models.CharField(max_length = 256)

class FirewallRoute(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    firewall = models.ForeignKey(Firewall, on_delete = models.CASCADE, default = False)
    ip_type = models.CharField(max_length = 256, choices = IpType.choices, default = IpType.IP)
    ip_area = models.CharField(max_length = 1024, choices = IpArea.choices, default = IpArea.IP4)
    ip_destination = models.CharField(max_length = 256)

class Phone(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 32768)
    number = models.CharField(max_length = 256)
    tarif = models.ForeignKey(Tarif, on_delete = models.CASCADE, default = False)

class NumberType(models.TextChoices):
    Number = 'NUMBER', 'number'
    Area = 'AREA', 'area'

class TarifRule(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    phone = models.ForeignKey(Phone, on_delete = models.CASCADE, default = False)
    number_type = models.CharField(max_length = 256, choices = NumberType.choices, default = NumberType.Number)
    number_destination = models.CharField(max_length = 256)

class User(models.Model):
    def __str__(self):
        return str(self.name)

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    email = models.CharField(max_length = 64)
    phone = models.CharField(max_length = 32)
    password = models.CharField(max_length = 128)
    tarif = models.ForeignKey(Tarif, on_delete = models.CASCADE, default = False)
