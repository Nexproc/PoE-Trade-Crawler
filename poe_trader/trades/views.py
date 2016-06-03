from django.shortcuts import render
from rest_framework import viewsets, permissions
from trades.serializers import TradeSerializer
from trades.models import Trade

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    permission_classes = [permissions.AllowAny,]
    serializer_class = TradeSerializer

