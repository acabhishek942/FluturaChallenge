from rest_framework import serializers

from stock_info_app.models import Stock

class StockSerializer(serializers.ModelSerializer):
    """
    Serializers solves two things.
    1. Converts to JSON
    2. Validations for the data passed
    """
    class Meta:
        model = Stock
        fields = '__all__'
        read_only_fields = [
            'symbol',
            'name',
            'market_capital',
            'sector',
            'industry'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)