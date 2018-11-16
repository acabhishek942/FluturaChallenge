from rest_framework import generics, mixins

from stock_info_app.models import Stock
from .serializers import StockSerializer

from django.core.cache import cache
from django.views.decorators.cache import cache_page

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

@cache_page(60 * 15)
class CachedStockListView(generics.ListAPIView):
    def get_queryset(self):
        return Stock.objects.all()

    def get_objects(self, queryset=None):
        stocks = cache.get() #add params for filtering
        if not stocks:
            stocks = super(CachedStockListView, self).get_objects(queryset)
            cache.set() #set values here
        return stocks
