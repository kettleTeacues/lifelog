from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_filters import rest_framework as djangoFilters

from rest_framework import viewsets, filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta

from lifelog.models import Lifelog
from .serializers import LifelogSerializer, LifelogWeekApiSerializer

@login_required
def index(request):
    context = {'userId': request.user.user_id}
    return render(request, 'index.html', context)

@login_required
def control(request):
    return render(request, 'lifelog/control.html')

def component(request):
    return render(request, 'lifelog/component.html')

class LifelogFilter(djangoFilters.FilterSet):
    class Meta:
        model = Lifelog
        fields = [
            'start_datetime',
            'end_datetime',
            'event'
        ]

# api用
class LifelogWeekApiView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LifelogWeekApiSerializer
    filter_backends = [djangoFilters.DjangoFilterBackend]
    filterset_class = LifelogFilter

    def get_queryset(self):
        userId = self.request.user.user_id
        urlDate = self.request.query_params.get('date').split('-')

        date = datetime(int(urlDate[0]), int(urlDate[1]), int(urlDate[2]))
        staDate = date - timedelta(days=7)
        endDate = date + timedelta(days=7)
        return Lifelog.objects.order_by(
                '-start_datetime'
            ).filter(
                created_by=userId,
                end_datetime__gte=staDate,
                start_datetime__lte=endDate
            )