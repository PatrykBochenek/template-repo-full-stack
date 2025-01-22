from django.shortcuts import render
from django import http
from clients import services
from .models import Client, AccountingPeriod

def index(request: http.HttpRequest) -> http.HttpResponse:
    return http.HttpResponse("Hello, world.")


def get_all_clients(request: http.HttpRequest) -> http.HttpResponse:
    data = services.get_all_clients(serialised=True)
    return http.JsonResponse(data, safe=False)

def get_client_account_periods(request: http.HttpRequest, client_id : int) -> http.HttpResponse:
    client = Client.objects.get(id = client_id)
    
    account_period = AccountingPeriod.objects.filter(client = client)

    data = list(account_period.values())

    return http.JsonResponse(data, safe=False)