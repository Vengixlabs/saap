from rest_framework import serializers
from .models import Posts


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ("id" , "title", "Description","created_at", "updated_at" , "label" , "link", "source" , "album")