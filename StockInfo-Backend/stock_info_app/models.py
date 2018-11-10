from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Stock(models.Model):
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    market_capital = models.FloatField()
    sector = models.CharField(max_length=50, null=True)
    industry = models.CharField(max_length=150, null=True)
    opening_price = models.FloatField(blank=True, default=0)
    closing_price = models.FloatField(blank=True, default=0)

    def get_api_url(self, request=None):
        return api_reverse("api-stocks:list-stocks", kwargs={'symbol':self.symbol}, request=request)