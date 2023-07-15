from django.shortcuts import render
from rest_framework import generics
from blog_post.models import BlogPost
from blog_post.serializers import BlogpostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated




class BlogpostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset=BlogPost.objects.all()
    serializer_class=BlogpostSerializer


class BlogpostUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset=BlogPost.objects.all()
    serializer_class=BlogpostSerializer

# Create your views here.
