from rest_framework import serializers

from .models import Post


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    author = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.author = validated_data.get("author", instance.author)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance