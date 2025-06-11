import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from .models import CallerInfo

from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import CallerInfo

def callers_list_api(request):
    """
    GET /api/callers/ → Returns a JSON list of all CallerInfo records.
    """
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    callers = CallerInfo.objects.order_by("-created_at").values(
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

    # If you need `created_at` as ISO strings:
    data = [
        { **c, "created_at": c["created_at"].isoformat() }
        for c in callers
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
def callers_webhook(request):
    """
    POST /api/callers/ → Telnyx will POST here.  We turn any missing/nulls
    into empty strings so nothing breaks our NOT NULL constraints.
    """
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    # 1) parse JSON
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    # 2) helper to clean each key
    def get_str(key):
        val = payload.get(key)
        return val if isinstance(val, str) else ""

    # 3) create & save
    try:
        ci = CallerInfo(
            caller_number    = get_str("caller_number"),
            main_path        = get_str("main_path"),
            caller_type      = get_str("caller_type"),
            business_name    = get_str("business_name"),
            practice_type    = get_str("practice_type"),
            primary_interest = get_str("primary_interest"),
            sales_email      = get_str("sales_email"),
            transcript       = get_str("transcript"),
        )
        ci.save()
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "success"}, status=201)
