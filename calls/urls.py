from django.urls import path
from . import views

urlpatterns = [
    # HTML view
    path("callers/", views.callers_table_view, name="callers_table"),

    # JSON GET API → returns a list of callers
    path(
        "api/callers/",
        views.callers_list_api,
        name="callers_list_api",
    ),

    # Telnyx webhook (POST only)
    path(
        "api/callers/webhook/",
        views.callers_webhook,
        name="callers_webhook",
    ),
]
