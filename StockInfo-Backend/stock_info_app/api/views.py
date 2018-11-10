from rest_framework import generics, mixins

from stock_info_app.models import Stock
from .serializers import StockSerializer


class StockListView(generics.ListAPIView):
    lookup_field = 'symbol'
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request':self.request}


class StockRetrieveVew(generics.RetrieveAPIView):
    lookup_field = 'symbol'
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.all()

    def get_object(self):
        symbol = self.kwargs.get("symbol")
        return Stock.objects.get(symbol=symbol)
