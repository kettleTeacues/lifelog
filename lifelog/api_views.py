from django_filters import rest_framework as djangoFilters
from rest_framework import viewsets, filters, generics

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

class LifelogFilter(djangoFilters.FilterSet):
    class Meta:
        model = Lifelog
        fields = [
            'staDate',
            'endDate',
            'event'
        ]

class LifelogListAPIView(generics.ListAPIView):
    serializer_class = LifelogSerializer
    filter_backends = [djangoFilters.DjangoFilterBackend]
    filterset_class = LifelogFilter

    def get_queryset(self):
        userId = self.request.user
        return Lifelog.objects.order_by('-staDate').filter(created_by=userId)