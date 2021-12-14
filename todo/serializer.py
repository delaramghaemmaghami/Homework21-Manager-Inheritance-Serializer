from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    categories = Category.objects.all()
    category = serializers.PrimaryKeyRelatedField(queryset=categories, many=True)

    class Meta:
        model = Task
        fields = "__all__"
