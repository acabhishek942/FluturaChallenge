from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stocks/', include('stock_info_app.api.urls', namespace='api-stocks')),
]