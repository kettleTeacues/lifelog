from rest_framework import serializers
from .models import Lifelog

class LifelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifelog
        isActive = serializers.ReadOnlyField(source='isActive')
        
        # すべてのフィールドをシリアライズ
        fields = [
            'staDate',
            'endDate',
            'event',
            'created_by',
            'created_at',
            'update_at',
            'isActive'
        ]
        read_only_fields = [
            'isActive'
        ]