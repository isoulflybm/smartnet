from django.apps import AppConfig
from django.apps import apps

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'
#    def ready(self):
#        print("Start firewall")
#        Firewall = apps.get_model(app_label = 'server', model_name = 'Firewall')
#        firewalls = Firewall.objects.values()
#        for firewall in firewalls:
#            pass
