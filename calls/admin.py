from django.contrib import admin
from .models import CallerInfo

@admin.register(CallerInfo)
class CallerInfoAdmin(admin.ModelAdmin):
    list_display = (
        "id", "call_id", "caller_number", "main_path", "caller_type",
        "business_name", "practice_type", "primary_interest", "sales_email",
        "client_inquiry_focus", "client_name",
        "account_identifier", "support_issue_summary", "callback_number",
        "created_at"
    )
    search_fields = ("call_id", "caller_number", "business_name", "client_name", "account_identifier")
    list_filter = ("main_path", "caller_type", "created_at")
