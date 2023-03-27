from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def index(request):
    blogs = Blog.objects.all()
    serialblogs = BlogSerializer(blogs, many=True)
    return Response(serialblogs.data)

@api_view(['GET'])
def blogView(request, pk):
    blog = Blog.objects.get(id=pk)
    serialblog = BlogSerializer(blog,many=False)
    return Response(serialblog.data)

@api_view(['POST'])
def blogAdd(request):
    serialdata = BlogSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)

@api_view(['POST'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serialblog = BlogSerializer(instance=blog, data=request.data)

    if serialblog.is_valid():
        serialblog.save()

    return Response(serialblog.data)
