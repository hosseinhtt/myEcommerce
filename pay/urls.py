from django.urls import path
from azbankgateways.urls import az_bank_gateways_urls
from pay.views import go_to_gateway_view, callback_gateway_view

urlpatterns = [
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view),
    path('callback-gateway/', callback_gateway_view)
]
