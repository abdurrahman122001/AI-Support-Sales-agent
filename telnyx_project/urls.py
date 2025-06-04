from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # Include the URLs defined in calls/urls.py
    path("", include("calls.urls")),
]
