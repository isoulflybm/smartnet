# Generated by Django 5.1 on 2024-11-03 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
