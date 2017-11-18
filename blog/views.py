from django.http import JsonResponse
from . import serializers
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView


from . import models
import json

# Create your views here.

class postListView(ListAPIView):
    serializer_class = serializers.PostSerializer
    
    def get_queryset(self):
        return models.Post.objects.all() 

class postRetrieveView(APIView):
    serializer_class = serializers.PostSerializer

    def get_object(self, pk):
        try:
            return models.Post.objects.get(pk=pk)
        except models.Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)

    # def get_object(self):
    #     obj = get_object_or_404(models.Post, pk=self.kwargs['pk'])
    #     return obj

class tagListView(ListAPIView):
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        return models.Tag.objects.all()

class CategoryView(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()