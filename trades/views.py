from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import detail_route, list_route
from trades.serializers import TradeSerializer, CurrencySerializer, HourlyTradeAggregateSerializer
from trades.models import Trade, Currency, HourlyTradeAggregate
from pprint import pprint
from datetime import datetime, timedelta


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trade.objects.select_related(
        'buy_currency',
        'sell_currency',
    ).all()
    serializer_class = TradeSerializer

    @list_route(methods=['get'])
    def trades_in_date_range(self, request):
        # work backwards from this date
        start_date = datetime.strptime(request.query_params.get('startDate'), '%Y-%m-%dT%H:%M:%S.%fZ')
        # day or hour
        range_type = request.query_params.get('rangeType')
        if range_type == 'hour':
            hourly_trade_aggregate = HourlyTradeAggregate.objects.filter(
                buy_currency_id=request.query_params.get('buyCurrencyId'),
                sell_currency_id=request.query_params.get('sellCurrencyId'),
                created__lte=start_date,
                created__gt=start_date - timedelta(hours=1),
            ).first()
        else:
            return response.Response('not yet implemented', status=status.HTTP_404_NOT_FOUND)

        trade_response = HourlyTradeAggregateSerializer(instance=hourly_trade_aggregate).data
        return response.Response(trade_response, status=status.HTTP_200_OK)


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
