from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clients/", views.get_all_clients, name="clients.list"),
    path("clients/create/", views.create_client, name="clients.create"),  # Add this line
    path(
        "clients/accounting-period/<int:client_id>/",
        views.get_client_account_periods,
        name="client.account-periods"
    ),
    path(
        "accounting-periods/create/",
        views.create_accounting_period,
        name="accounting-periods.create"
    ),
]