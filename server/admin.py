from django.contrib import admin

# Register your models here.

from .models import User
from .models import Tarif
from .models import Firewall
from .models import FirewallRestriction

admin.site.register(User)
admin.site.register(Tarif)
admin.site.register(Firewall)
admin.site.register(FirewallRestriction)
