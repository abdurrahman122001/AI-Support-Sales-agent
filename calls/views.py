from django.shortcuts import render
from .models import CallerInfo

def callers_table_view(request):
    """
    Renders an HTML page with a table of all CallerInfo records.
    """
    callers = CallerInfo.objects.all().order_by("-created_at")
    return render(request, "calls/callers_table.html", {"callers": callers})
