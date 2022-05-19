#account/serializers.py
from rest_framework import serializers
from .models import account

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = account        # account 모델 사용
        fields = '__all__'            # 모든 필드 포함