from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    post_count = serializers.IntegerField(required=False)

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    post_count = serializers.IntegerField(required=False)
