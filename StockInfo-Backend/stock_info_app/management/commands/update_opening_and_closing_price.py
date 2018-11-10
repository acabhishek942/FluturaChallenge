from django.core.management.base import BaseCommand, CommandError
import requests
import simplejson as json

from stock_info_app.models import Stock

from datetime import date, timedelta
import time

class Command(BaseCommand):
    """
    This utility function should run as a background process everyday after the market closes
    """
    help = 'Updates the opening and closing price of all the stocks in DB'


    def handle(self, *args, **options):
        all_stocks = Stock.objects.all()
        print(len(all_stocks))
        counter = 0
        aplha_advantage_api_keys = ['SQ19E6KPE7TC636A', 'KDPSEUJERAQ3TG4S', 'PSKRI5TCCBJY02KO', 'RRA8ZBOWYCW83ROZ', '4MEZMR6Y2CS3O4OV', 'R4PHUMAY9OE9B1QP'] # ideally this key should be hidden but since it is a free key it is visible to all
        get_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=<symbol>&apikey=' + aplha_advantage_api_keys[counter]
        for stock in all_stocks:
            alpha_advantage_api_response = requests.get(get_url.replace('<symbol>', stock.symbol))
            jsonified_response = json.loads(alpha_advantage_api_response.text)
            if (len(jsonified_response.keys()) == 1):
                counter += 1
                get_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=<symbol>&apikey=' + aplha_advantage_api_keys[counter]
                alpha_advantage_api_response = requests.get(get_url.replace('<symbol>', stock.symbol))
                jsonified_response = json.loads(alpha_advantage_api_response.text)
                if (len(jsonified_response.keys()) == 1):
                    counter = 0
                    time.sleep(60)
            try:
                stock.opening_price = float(jsonified_response['Time Series (Daily)'][str(date.today() - timedelta(1))]['1. open'])
                stock.closing_price = float(jsonified_response['Time Series (Daily)'][str(date.today() - timedelta(1))]['4. close'])
                stock.save()
            except KeyError:
                pass #ideally we should not pass silently