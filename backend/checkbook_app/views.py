from rest_framework.viewsets import ModelViewSet
from .serializers import CheckbookSerializer
from .models import Checkbook

class CheckbookViewSet(ModelViewSet):
    queryset = Checkbook.objects.all()
    serializer_class = CheckbookSerializer
