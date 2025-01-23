from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from . import services
from .models import Client
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt  # Only for development
@require_http_methods(["POST"])
def create_client(request: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(request.body)

        if not data.get('code'):
            return JsonResponse(
                {"status": "error", "message": "code is required"},
                status=400
            )
        
        if Client.objects.filter(code=data['code']).exists():
            return JsonResponse(
                {"status": "error", "message": "Client code must be unique"},
                status=400
            )
        
        client = Client.objects.create(
            code=data['code'],
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            is_active=data.get('is_active', True) 
        )
        
        return JsonResponse({
            "status": "success",
            "data": {
                "id": client.id,
                "code": client.code,
                "name": client.name,
                "email": client.email,
                "phone": client.phone,
                "is_active": client.is_active,
                "created_at": client.created_at.isoformat() if client.created_at else None,
                "updated_at": client.updated_at.isoformat() if client.updated_at else None
            }
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON data"},
            status=400
        )
    except ValidationError as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=400
        )
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )