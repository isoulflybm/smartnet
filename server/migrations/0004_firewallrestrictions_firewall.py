# Generated by Django 5.1 on 2024-11-09 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_firewall_firewallrestrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='firewallrestrictions',
            name='Firewall',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='server.firewall'),
        ),
    ]