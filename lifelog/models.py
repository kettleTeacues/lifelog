from django.db import models
from django.conf import settings
from django.utils import timezone

import datetime, uuid

class Lifelog(models.Model):
    record_key = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    start_datetime = models.DateTimeField(null = True)
    end_datetime = models.DateTimeField(null = True)
    event = models.CharField(blank=True, null=True, max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def isActive(self):
        return False

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['start_datetime', 'end_datetime', 'event', 'created_by'],
                name='unique_log'
            )
        ]

    def __str__(self):
        return str(self.created_by)+' '+self.event+' '+format(self.start_datetime, '%Y-%m-%d %H-%M-%S')