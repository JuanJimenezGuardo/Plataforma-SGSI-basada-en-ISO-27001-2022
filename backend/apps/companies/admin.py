from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rfc', 'email', 'city', 'country')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'rfc', 'email')
    ordering = ('-created_at',)

