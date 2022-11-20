from rest_framework import serializers
from .models import Lifelog

class LifelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifelog
        
        # すべてのフィールドをシリアライズ
        exclude = ()