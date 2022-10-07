from rest_framework import serializers 
from .models import Checkbook

class CheckbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbook
        fields = ['id', 'type', 'name', 'trans_date', 'amount', 'total_credits', 'total_debits', 'balance']
        

