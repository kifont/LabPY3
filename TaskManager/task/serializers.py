from rest_framework import serializers
from task.models import Task, Category
from django.contrib.auth.models import User


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['category_name']
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['category', 'Title', 'Desc', 'Deadline', 'Priority', 'Status', 'Date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_category(self, value):

        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Обрана категорія не існує.")
        return value