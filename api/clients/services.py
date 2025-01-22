from . import models
from django.db.models import QuerySet


def get_all_clients(serialised=False) -> QuerySet[models.Client] | list[dict[str, str]]:
    qs = models.Client.objects.all()
    if not serialised:
        return qs
    return list(qs.values("code", "id"))
