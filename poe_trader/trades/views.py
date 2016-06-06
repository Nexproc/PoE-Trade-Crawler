from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import detail_route, list_route
from trades.serializers import TradeSerializer, CurrencySerializer
from trades.models import Trade, Currency
from pprint import pprint
from datetime import datetime


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.select_related(
        'buy_currency',
        'sell_currency',
    ).all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = TradeSerializer

    @list_route(methods=['get'])
    def trades_in_date_range(self, request):
        # work backwards from this date
        start_date = datetime.strptime(request.query_params.get('startDate'), '%Y-%m-%dT%H:%M:%S.%fZ')
        # day or hour
        range_type = request.query_params.get('rangeType')
        trade_queryset = Trade.objects.all()
        trade_queryset = getattr(Trade, 'trades_in_past_{}'.format(range_type))(
            date=start_date,
            queryset=trade_queryset,
        )
        trade_queryset = Trade.trades_between_currencies(
            buy_currency_id=request.query_params.get('buyCurrencyId'),
            sell_currency_id=request.query_params.get('sellCurrencyId'),
            queryset=trade_queryset,
        )
        trade_response = Trade.get_highest_average_and_lowest_trade(queryset=trade_queryset)
        return response.Response(trade_response, status=status.HTTP_200_OK)


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CurrencySerializer
