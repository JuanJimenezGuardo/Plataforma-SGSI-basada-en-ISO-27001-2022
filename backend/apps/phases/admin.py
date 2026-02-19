from django.contrib import admin
from .models import Phase


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'type', 'start_date', 'end_date', 'order')
    list_filter = ('type', 'project', 'created_at')
    search_fields = ('name', 'description', 'project__name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('project', 'order')
