# Generated by Django 5.1.3 on 2024-11-28 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordonnance',
            options={'ordering': ('-id',)},
        ),
        migrations.RemoveField(
            model_name='ordonnance',
            name='user',
        ),
        migrations.AlterModelTable(
            name='ordonnance',
            table='ordonnances',
        ),
    ]
