# Generated by Django 5.1.6 on 2025-04-05 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyInventoryApp', '0002_account_alter_waterbottle_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='password',
            new_name='password1',
        ),
    ]
