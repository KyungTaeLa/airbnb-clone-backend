from rest_framework import serializers
from .models import Category

# ModelSerializer의 Meta 를 통해 category 모델의 전체 fields 를 가져옴
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # 일부 필드만 보기
        # fields = ("name", "kind")
        fields = "__all__"
 