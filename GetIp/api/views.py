from rest_framework.views import APIView
from GetIp.api.serializers import IpSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from GetIp.models import IPs

class GetIpAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('HTTP_CF_CONNECTING_IP') or request.META.get('REMOTE_ADDR')

        ip_address = ip      
        serialize = IpSerializer(data=ip_address)
        IPs.objects.create(ip=ip_address)
        if serialize.is_valid():
            return JsonResponse(data=serialize.validated_data, status=status.HTTP_200_OK)
        return JsonResponse(data={
            'ip':ip_address
        },status=status.HTTP_200_OK)