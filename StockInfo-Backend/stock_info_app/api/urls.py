from django.urls import path

from .views import StockListView, StockRetrieveVew

app_name = 'postings'

urlpatterns = [
    path('', StockListView.as_view(), name='list-stocks'),
    path('<slug:symbol>/', StockRetrieveVew.as_view(), name='stock-view'),
]