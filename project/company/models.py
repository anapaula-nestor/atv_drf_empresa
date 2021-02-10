from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    trading_name = models.CharField(max_length=255, null=False, blank=False)
    sector = models.CharField(max_length=100)
    registered_number = models.IntegerField(null=False, unique=True)
    IE_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(null=False, default=False)

    def __str__(self):
            return f'{self.registered_number} - {self.company_name}'
