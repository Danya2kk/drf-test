from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #
    #     if not pk:
    #         return Post.objects.all()
    #
    #     return Post.objects.filter(pk=pk)
    #
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if pk is not None:
#             try:
#                 post = Post.objects.get(pk=pk)
#                 serializer = PostSerializer(post)
#                 return Response({'post': serializer.data})
#             except:
#                 return Response({'error': 'Объект не найден'})
#         else:
#             posts = Post.objects.all()
#             serializer = PostSerializer(posts, many=True)
#             return Response({'posts': serializer.data})
#
#     # def get(self, request):
#     #     p = Post.objects.all()
#     #
#     #     return Response({'posts': PostSerializer(p, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Обьект не найден"})
#
#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'метод DELETE не разрешен'})
#         try:
#             instance = Post.objects.get(pk=pk).delete()
#             return Response({'message': 'Удалены данные с id ' + str(pk)})
#
#         except:
#             return Response({'error': 'Объект не найден'})


