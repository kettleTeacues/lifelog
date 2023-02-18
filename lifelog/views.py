import pytz

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_filters import rest_framework as djangoFilters
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta

from lifelog.models import Lifelog, about
from .serializers import LifelogSpanApiSerializer, aboutSerializer

@login_required
def index(request):
    context = {'userId': request.user.user_id}
    return render(request, 'index.html', context)

class LifelogFilter(djangoFilters.FilterSet):
    class Meta:
        model = Lifelog
        fields = [
            'start_datetime',
            'end_datetime',
            'event'
        ]

# api用
class LifelogSpanApiView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LifelogSpanApiSerializer
    filter_backends = [djangoFilters.DjangoFilterBackend]
    filterset_class = LifelogFilter

    def get_queryset(self):
        userId = self.request.user.user_id
        urlDate = self.request.query_params.get('date').split('-')
        urlCalendarSpan = self.request.query_params.get('span')

        date = datetime(int(urlDate[0]), int(urlDate[1]), int(urlDate[2]), tzinfo=pytz.timezone('Asia/Tokyo'))
        staDate = date - timedelta(days=7)
        endDate = date + timedelta(days=7)
        if urlCalendarSpan == 'month':
            staDate = date - timedelta(days=40)
            endDate = date + timedelta(days=40)
        if urlCalendarSpan == 'day':
            staDate = date
            endDate = date + timedelta(days=1)
        print(f'today  : {date}')
        print(f'staDate: {staDate}')
        print(f'endDate: {endDate}')
        return Lifelog.objects.order_by(
                '-start_datetime'
            ).filter(
                created_by=userId,
                end_datetime__gte=staDate,
                start_datetime__lte=endDate
            )

class aboutApiView(generics.ListAPIView):
    serializer_class = aboutSerializer
    def get_queryset(self):
        return about.objects.all()