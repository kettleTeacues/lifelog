from rest_framework import viewsets, filters
from .models import Lifelog
from .serializers import LifelogSerializer

class LifelogViewSet(viewsets.ModelViewSet):
    queryset = Lifelog.objects.all()
    serializer_class = LifelogSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        'id',
        'staDate',
    )
    ordering = (
        'endDate'
    )