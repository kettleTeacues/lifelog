from django_filters import rest_framework as djangoFilters
from rest_framework import viewsets, filters, generics
from rest_framework.pagination import PageNumberPagination

from .models import Lifelog
from .serializers import LifelogSerializer

class LifelogViewSet(viewsets.ModelViewSet):
    queryset = Lifelog.objects.all()
    serializer_class = LifelogSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        'id',
        'start_datetime',
    )
    ordering = (
        'end_datetime'
    )

class LifelogFilter(djangoFilters.FilterSet):
    class Meta:
        model = Lifelog
        fields = [
            'start_datetime',
            'end_datetime',
            'event'
        ]

class defaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    max_page_size = 1000

class LifelogListAPIView(generics.ListAPIView):
    serializer_class = LifelogSerializer
    filter_backends = [djangoFilters.DjangoFilterBackend]
    filterset_class = LifelogFilter
    pagination_class = defaultPagination

    def get_queryset(self):
        userId = self.request.user.user_id
        return Lifelog.objects.order_by('-start_datetime').filter(created_by=userId)