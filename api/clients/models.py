from django.db import models
from django.core.exceptions import ValidationError

class Client(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"

class AccountingPeriod(models.Model):
    BOOKKEEPING_SYSTEMS = [
        ('QB', 'QuickBooks'),
        ('XE', 'Xero'),
        ('SP', 'Sage'),
        ('FW', 'FreshWorks'),
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    bookkeeping_system = models.CharField(
        max_length=2,
        choices=BOOKKEEPING_SYSTEMS,
        default='QB'
    )
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
        related_name='accounting_periods'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('DRAFT', 'Draft'),
            ('IN_PROGRESS', 'In Progress'),
            ('COMPLETED', 'Completed'),
            ('ARCHIVED', 'Archived')
        ],
        default='DRAFT'
    )
    notes = models.TextField(blank=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be greater than end date")
        overlapping = AccountingPeriod.objects.filter(
            client=self.client,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(id=self.id)
        if overlapping.exists():
            raise ValidationError("Accounting period overlaps with existing period")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)