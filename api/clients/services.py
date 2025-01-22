from typing import List, Dict, Any, Optional
from django.db.models import Q
from .models import Client, AccountingPeriod

def get_all_clients(serialised: bool = False) -> List[Dict[str, Any]]:
    """
    Retrieve all active clients.
    """
    clients = Client.objects.filter(is_active=True)
    if serialised:
        return list(clients.values())
    return list(clients)

def create_client(data: Dict[str, Any]) -> Client:
    """
    Create a new client with validation.
    """
    client = Client(**data)
    client.full_clean()
    client.save()
    return client

def get_client_accounting_periods(
    client_id: int,
    status: Optional[str] = None
) -> List[AccountingPeriod]:
    """
    Get accounting periods for a client with optional status filter.
    """
    query = Q(client_id=client_id)
    if status:
        query &= Q(status=status)
    
    return list(AccountingPeriod.objects.filter(query))