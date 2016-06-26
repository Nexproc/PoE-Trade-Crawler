from django.db import models
from django.db.models import Min, Max, Avg
from decimal import Decimal
from core.constants import CURRENCIES
from datetime import timedelta


class Currency(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    @classmethod
    def update_lookup_table(cls):
        old_currencies = cls.objects.values_list('id', 'name')
        old_currencies_lookup = {name: id for id, name in old_currencies}

        for new_id, name in CURRENCIES.items():
            currency, _ = cls.objects.get_or_create(
                id=new_id,
            )

            currency.name = name
            currency.save()

            old_buys = Trade.objects.select_related(
                'buy_currency',
            ).filter(
                buy_currency_id=old_currencies_lookup.get(name),
            ).update(
                buy_currency_id=new_id,
            )

            old_sales = Trade.objects.select_related(
                'sell_currency',
            ).filter(
                sell_currency_id=old_currencies_lookup.get(name),
            ).update(
                sell_currency_id=new_id,
            )


# Create your models here.
class Trade(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    sell_currency = models.ForeignKey(Currency, related_name='selling_trades')
    buy_currency = models.ForeignKey(Currency, related_name='buying_trades')
    sell_value = models.DecimalField(decimal_places=6, max_digits=20)
    buy_value = models.DecimalField(decimal_places=6, max_digits=20)
    trade_ratio = models.DecimalField(decimal_places=6, max_digits=20)

    def set_sell_currency(self, sell_currency):
        self.sell_currency_id = sell_currency

    def set_buy_currency(self, buy_currency):
        self.buy_currency_id = buy_currency

    def set_sell_value(self, sell_value):
        self.sell_value = sell_value

    def set_buy_value(self, buy_value):
        self.buy_value = buy_value

    def set_trade_ratio(self):
        self.trade_ratio = Decimal(self.sell_value) / Decimal(self.buy_value)

    def stringify_and_print(self):
        print("Sell Currency: {}".format(CURRENCIES[int(self.sell_currency)]))
        print("Sell Value: {}".format(self.sell_value))
        print("Buy Currency: {}".format(CURRENCIES[int(self.buy_currency)]))
        print("Buy Value: {}".format(self.buy_value))
        print("Trade Ratio: {}".format(self.trade_ratio))

    @classmethod
    def trades_in_past_hour(cls, date, queryset):
        return queryset.filter(
            created__lt=date,
            created__gte=(date - timedelta(hours=1)),
        )

    @classmethod
    def trades_in_past_day(cls, date, queryset):
        return queryset.filter(
            created__lt=date,
            created__gte=(date - timedelta(days=1)),
        )

    @classmethod
    def trades_between_currencies(cls, buy_currency_id, sell_currency_id, queryset):
        # this method assumes that you've already created a queryset
        return queryset.filter(
            buy_currency_id=buy_currency_id,
            sell_currency_id=sell_currency_id,
        )

    @classmethod
    def get_highest_average_and_lowest_trade(cls, queryset):
        # this method assumes that you've done the other filtering yourself (currency, dates, etc)
        return queryset.aggregate(
            low=Min('trade_ratio'),
            high=Max('trade_ratio'),
            average=Avg('trade_ratio'),
        )

    def __repr__(self):
        return '<{}:{} {}>'.format(self.__class__.__name__, self.pk, str(self))

class HourlyTradeAggregate(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    sell_currency = models.ForeignKey(Currency, related_name='hourly_sells')
    buy_currency = models.ForeignKey(Currency, related_name='hourly_buys')
    low_ratio = models.DecimalField(decimal_places=6, max_digits=20)
    average_ratio = models.DecimalField(decimal_places=6, max_digits=20)
    high_ratio = models.DecimalField(decimal_places=6, max_digits=20)
    number_of_trades = models.PositiveIntegerField()

    @classmethod
    def create_trade_aggregations_for_this_hour(cls):
        # aggregate trades by currency combinations
        for buy_currency_id in CURRENCIES.keys():
            for sell_currency_id in CURRENCIES.keys():
                # filter trades by buy and sell
                # create aggregate data dictionary
                hourly_aggregates = Trade.objects.filter(
                    buy_currency_id=buy_currency_id,
                    sell_currency_id=sell_currency_id,
                ).aggregate(
                    hour_created=models.Min('created'),
                    low=models.Min('trade_ratio'),
                    high=models.Max('trade_ratio'),
                    average=models.Avg('trade_ratio'),
                    total=models.Count('id'),
                )

                # create aggregate data object
                if hourly_aggregates.get('total'):
                    new_hourly_object = HourlyTradeAggregate.objects.create(
                        buy_currency_id=buy_currency_id,
                        sell_currency_id=sell_currency_id,
                        low_ratio=hourly_aggregates.get('low'),
                        average_ratio=hourly_aggregates.get('average'),
                        high_ratio=hourly_aggregates.get('high'),
                        number_of_trades=hourly_aggregates.get('total'),
                    )
