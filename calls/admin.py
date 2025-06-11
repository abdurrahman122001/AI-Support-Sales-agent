from django.contrib import admin
from .models import CallerInfo

@admin.register(CallerInfo)
class CallerInfoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "caller_number",
        "main_path",
        "caller_type",
        "business_name",
        "practice_type",
        "primary_interest",
        "sales_email",
        "transcript",
        "created_at",
    )
    list_filter = ("main_path", "caller_type", "business_name")
    search_fields = ("caller_number", "business_name", "sales_email")
    ordering = ("-created_at",)
