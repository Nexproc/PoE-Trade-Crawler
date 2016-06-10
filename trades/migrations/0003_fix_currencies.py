from __future__ import unicode_literals

from django.db import migrations
from core.constants import CURRENCIES
from trades.models import Currency

def fix_trades(apps, *_, **__):
    currencies = Currency.objects.all()
    for currency in currencies:
        currency.name = currency.id
        currency.save()

    for currency in currencies:
        currency.name = CURRENCIES[currency.id]
        currency.save()



class Migration(migrations.Migration):
    dependencies = [
        ('trades', '0002_populate_currencies'),
    ]

    operations = [
        migrations.RunPython(fix_trades)
    ]
