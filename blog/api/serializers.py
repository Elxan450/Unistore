from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            "title",
            "description",
            "image", 
            "created_at", 
            "slug"
        )
