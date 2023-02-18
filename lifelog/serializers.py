from rest_framework import serializers

from . import models

class LifelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lifelog
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

class LifelogSpanApiSerializer(serializers.Serializer):
    id = serializers.CharField()
    start = serializers.DateTimeField(source='start_datetime', format='%Y-%m-%d %H:%M:%S')
    end = serializers.DateTimeField(source='end_datetime', format='%Y-%m-%d %H:%M:%S')
    name = serializers.CharField(source='event')
    detail = serializers.CharField()
    color = serializers.CharField()

    class Meta:
        model = models.Lifelog
        isActive = serializers.ReadOnlyField(source='isActive')

        fields = [
            'id',
            'start_datetime',
            'end_datetime',
            'event',
            'detail',
            'color'
        ]

class tagApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tag

        exclude = [
            'created_by'
        ]

class memoApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.memo

        exclude = [
            'created_by'
        ]

class aboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.about
        html = serializers.ReadOnlyField(source='html')
        fields = [
            'html'
        ]