from django.urls import path
from .views import callers_table_view

urlpatterns = [
    path("callers/", callers_table_view, name="callers-table"),
]
