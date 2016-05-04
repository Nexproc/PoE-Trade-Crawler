from django.db import models
from decimal import Decimal
from core.constants import CURRENCIES

class Currency(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

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
        self.trade_ratio = Decimal(self.sell_value)/Decimal(self.buy_value)

    def stringify_and_print(self):
        print("Sell Currency: {}".format(CURRENCIES[int(self.sell_currency)]))
        print("Sell Value: {}".format(self.sell_value))
        print("Buy Currency: {}".format(CURRENCIES[int(self.buy_currency)]))
        print("Buy Value: {}".format(self.buy_value))
        print("Trade Ratio: {}".format(self.trade_ratio))

    def __repr__(self):
        return '<{}:{} {}>'.format(self.__class__.__name__, self.pk, str(self))