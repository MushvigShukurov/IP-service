from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-my-ip/',include('GetIp.api.urls')),
    path('', include("GetIp.api.urls")),
]
