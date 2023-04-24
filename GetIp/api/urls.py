from django.urls import path 
from GetIp.api.views import GetIpAPIView
urlpatterns = [
    path('',GetIpAPIView.as_view(), name='yout-ip-address'),
]