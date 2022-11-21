from django.db import models
from django.conf import settings
from django.utils import timezone

class Lifelog(models.Model):
    staDate = models.DateTimeField(null = True)
    endDate = models.DateTimeField(null = True)
    event = models.CharField(blank=True, null=True, max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
