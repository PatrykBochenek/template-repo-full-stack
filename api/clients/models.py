from django.db import models


# Create your models here.
class Client(models.Model):
    code = models.CharField(max_length=255)


class AccountingPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    bookkeeping_system = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
