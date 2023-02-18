from django.db import models
from django.conf import settings
from django.utils import timezone

import datetime, uuid

class tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(blank=True, null=True, max_length=20)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

class Lifelog(models.Model):
    record_key = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    start_datetime = models.DateTimeField(null = True)
    end_datetime = models.DateTimeField(null = True)
    event = models.CharField(blank=True, null=True, max_length=100)
    detail = models.CharField(blank=True, null=True, max_length=255)
    color = models.CharField(blank=True, null=True, max_length=20)
    tags = models.ManyToManyField(to=tag)
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

class memo(models.Model):
    content = models.TextField()
    is_archived = models.BooleanField(default=False)
    event = models.ForeignKey(
        Lifelog,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

class about(models.Model):
    html = models.TextField()