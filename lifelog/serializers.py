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

class LifelogWeekApiSerializer(serializers.Serializer):
    id = serializers.CharField()
    start = serializers.DateTimeField(source='start_datetime', format='%Y-%m-%d %H:%M:%S')
    end = serializers.DateTimeField(source='end_datetime', format='%Y-%m-%d %H:%M:%S')
    event = serializers.CharField()
    isActive = serializers.BooleanField()

    class Meta:
        model = Lifelog
        isActive = serializers.ReadOnlyField(source='isActive')

        fields = [
            'id',
            'start_datetime',
            'end_datetime',
            'event',
            'isActive'
        ]