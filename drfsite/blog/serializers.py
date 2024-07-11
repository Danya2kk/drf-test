from rest_framework import serializers

from .models import Post, Category, Comment


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


    def get_comments(self, obj):
        latest_comments = obj.comments.all().order_by('-time_create')[:3]
        return CommentSerializer(latest_comments, many=True).data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    latest_replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'parent', 'content', 'author', 'time_create', 'latest_replies']


    def get_latest_replies(self, obj):
        latest_replies = obj.replies.all().order_by('-time_create')[:3]
        return CommentSerializer(latest_replies, many=True).data

# class PostSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     author = serializers.CharField(max_length=255)
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.author = validated_data.get("author", instance.author)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance