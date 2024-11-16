from django.contrib import admin

# Register your models here.

from .models import User
from .models import Tarif
from .models import Firewall
from .models import FirewallRestriction
from .models import FirewallRoute
from .models import Phone
from .models import TarifRule

admin.site.register(User)
admin.site.register(Tarif)
admin.site.register(Firewall)
admin.site.register(FirewallRestriction)
admin.site.register(FirewallRoute)
admin.site.register(Phone)
admin.site.register(TarifRule)
