from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name','trading_name', 'sector', 'registered_number','IE_number', 'created_at','updated_at','is_active')


admin.site.register(Company,CompanyAdmin)
