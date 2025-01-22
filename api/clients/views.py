from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from . import services
from .models import Client

@require_http_methods(["GET"])
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to the Accounting API")

@require_http_methods(["GET"])
def get_all_clients(request: HttpRequest) -> JsonResponse:
    try:
        data = services.get_all_clients(serialised=True)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )

@require_http_methods(["GET"])
def get_client_account_periods(
    request: HttpRequest,
    client_id: int
) -> JsonResponse:
    try:
        client = get_object_or_404(Client, id=client_id)
        status = request.GET.get('status')
        
        account_periods = services.get_client_accounting_periods(
            client_id,
            status=status
        )
        
        serialized_periods = []
        for period in account_periods:
            serialized_periods.append({
                'id': period.id,
                'start_date': period.start_date,
                'end_date': period.end_date,
                'status': period.status,
                'bookkeeping_system': period.bookkeeping_system,
            })
        
        return JsonResponse({
            "status": "success",
            "data": serialized_periods
        })
    except Client.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Client not found"},
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )