from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json

from lifelog.models import Lifelog

@login_required
def index(request):
    context = {'userId': request.user.user_id}
    return render(request, 'lifelog/index.html', context)

@login_required
def control(request):
    return render(request, 'lifelog/control.html')