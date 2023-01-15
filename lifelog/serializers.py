from rest_framework import serializers
from .models import Lifelog

class LifelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifelog
        isActive = serializers.ReadOnlyField(source='isActive')
        
        # すべてのフィールドをシリアライズ
        fields = [
            'id',
            'start_datetime',
            'end_datetime',
            'event',
            'created_by',
            'created_at',
            'updated_at',
            'isActive'
        ]
        read_only_fields = [
            'isActive'
        ]