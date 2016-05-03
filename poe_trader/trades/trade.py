from decimal import Decimal
from poe_trader.core.constants import CURRENCIES

class Trade:
    sell_currency = None
    buy_currency = None
    sell_value = 0
    buy_value = 0
    trade_ratio = 0

    def __init__(self):
        pass

    def set_sell_currency(self, sell_currency):
        self.sell_currency = sell_currency

    def set_buy_currency(self, buy_currency):
        self.buy_currency = buy_currency

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