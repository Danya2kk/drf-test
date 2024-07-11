from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


# Create your views here.


# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if pk is not None:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post)
                return Response({'post': serializer.data})
            except:
                return Response({'error': 'Объект не найден'})
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response({'posts': serializer.data})

    # def get(self, request):
    #     p = Post.objects.all()
    #
    #     return Response({'posts': PostSerializer(p, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Обьект не найден"})

        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'метод DELETE не разрешен'})
        try:
            instance = Post.objects.get(pk=pk).delete()
            return Response({'message': 'Удалены данные с id ' + str(pk)})

        except:
            return Response({'error': 'Объект не найден'})


