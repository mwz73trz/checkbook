from django.db import models
from django.db.models import Sum

class Checkbook(models.Model):
    DEBIT = 'Debit'
    CREDIT = 'Credit'
    TYPES = [(DEBIT, 'Debit'), (CREDIT, 'Credit')]
    type = models.CharField(max_length=6, choices=TYPES)
    name = models.CharField(max_length=50)
    trans_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def total_debits(self):
        return Checkbook.objects.filter(type='Debit').aggregate(total_debits=Sum('amount'))

    @property
    def total_credits(self):
        return Checkbook.objects.filter(type='Credit').aggregate(total_credits=Sum('amount'))

    @property
    def balance(self):
        return self.total_credits['total_credits'] - self.total_debits['total_debits']

    def __str__(self):
        return f'{self.name}'
