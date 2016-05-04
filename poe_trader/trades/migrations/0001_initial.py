# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sell_value', models.DecimalField(decimal_places=6, max_digits=20)),
                ('buy_value', models.DecimalField(decimal_places=6, max_digits=20)),
                ('trade_ratio', models.DecimalField(decimal_places=6, max_digits=20)),
                ('buy_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buying_trades', to='trades.Currency')),
                ('sell_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selling_trades', to='trades.Currency')),
            ],
        ),
    ]
