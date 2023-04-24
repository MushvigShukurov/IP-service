from django.db import models

# Create your models here.


class IPs(models.Model):
    ip = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Clients"
    def __str__(self) -> str:
        return self.ip
