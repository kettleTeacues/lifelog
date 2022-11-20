from django.shortcuts import render
from django.views.decorators.http import require_safe

from lifelog.models import Lifelog

@require_safe
def index(request):
    lifelog = Lifelog.objects.all()
    context = {'lifelog': lifelog}
    return render(request, 'lifelog/index.html', context)
