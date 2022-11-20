from django.db import models
from django.conf import settings

class Lifelog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    event = models.CharField(blank=True, default='', max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    update_at = models.DateTimeField(auto_now=True)
