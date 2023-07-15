from rest_framework import serializers
from blog_post.models import BlogPost

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

