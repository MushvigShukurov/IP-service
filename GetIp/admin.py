from django.contrib import admin

from GetIp.models import IPs

# admin.site.register(IPs)

@admin.register(IPs)
class IpsAdmin(admin.ModelAdmin):
    list_display = ['ip','created_at']