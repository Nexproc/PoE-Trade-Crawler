from rest_framework import serializers
from trades.models import Trade, Currency, HourlyTradeAggregate

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
            'id',
            'sell_currency_name',
            'buy_currency_name',
            'sell_value',
            'buy_value',
            'trade_ratio',
        )

    sell_currency_name = serializers.SerializerMethodField()
    buy_currency_name = serializers.SerializerMethodField()

    @staticmethod
    def get_sell_currency_name(obj):
        return obj.sell_currency.name

    @staticmethod
    def get_buy_currency_name(obj):
        return obj.buy_currency.name


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
        )

class HourlyTradeAggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyTradeAggregate
        fields = (
            'id',
            'average',
            'high',
            'low',
        )

    average = serializers.SerializerMethodField()
    high = serializers.SerializerMethodField()
    low = serializers.SerializerMethodField()

    @staticmethod
    def get_average(obj):
        return obj.average_ratio

    @staticmethod
    def get_high(obj):
        return obj.high_ratio

    @staticmethod
    def get_low(obj):
        return obj.low_ratio
