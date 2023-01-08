from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json

from lifelog.models import Lifelog

@login_required
def index(request):
    lifelog = Lifelog.objects.order_by('-start_datetime').filter(created_by=request.user.user_id)

    context = {'userId': request.user.user_id}
    return render(request, 'lifelog/index.html', context)

@login_required
def control(request):
    return render(request, 'lifelog/control.html')