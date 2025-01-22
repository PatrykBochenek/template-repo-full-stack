from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clients/", views.get_all_clients, name="clients.list"),
    path(
        "clients/<int:client_id>/accounting-periods/",
        views.get_client_account_periods,
        name="client.account-periods"
    ),
]