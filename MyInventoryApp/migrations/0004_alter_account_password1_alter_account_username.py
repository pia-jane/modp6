# Generated by Django 5.1.6 on 2025-04-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyInventoryApp', '0003_rename_password_account_password1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
