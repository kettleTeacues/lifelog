from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe

import json

from lifelog.models import Lifelog
from lifelog.serializers import LifelogSerializer

@login_required
def index(request):
    lifelog = Lifelog.objects.order_by('-staDate').filter(created_by=request.user.id)
    serializer = LifelogSerializer(lifelog, many=True)

    context = {'lifelog': json.dumps(serializer.data, ensure_ascii=False)}
    return render(request, 'lifelog/index.html', context)

@login_required
def control(request):
    return render(request, 'lifelog/control.html')