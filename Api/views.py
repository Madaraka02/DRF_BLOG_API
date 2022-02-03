from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]

