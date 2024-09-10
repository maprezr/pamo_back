from apps.master_price.api import api
from django.urls import path

urlpatterns = [
    path("list_products", api.masterPriceAPIView.as_view(), name="list_products"),
    path("oaut_meli", api.OAuthAPIView.as_view(), name="oaut_meli"),
    path("notification_shopi", api.NotificationHandlerShopífy.as_view(), name="wh_shopi"),
    path("notification_meli", api.NotificationHandlerMeli.as_view(), name="wh_meli"),
]