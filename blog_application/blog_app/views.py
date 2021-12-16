from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User,blog_category,blog
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from .serializers import *


@api_view(['POST'])
def add_category(request):
    if request.method=="POST":
        category_name=request.data.get("category_name")
        c=blog_category.objects.create(category_name=category_name)

        obj=blog_category.objects.filter(id=c.id)
        ser=blog_category_serialiser(obj,many=True)
        return Response(ser.data)
    return Response("Please fill the form")


@api_view(['GET'])
def get_category(request):
    obj=blog_category.objects.all()
    ser=blog_category_serialiser(obj,many=True)
    return Response(ser.data)

@api_view(['DELETE'])
def del_category(request,id):
    d=blog_category.objects.filter(id=id)
    d.delete()
    return Response("Deleted")

@api_view(['PUT'])
def upd_dategory(request,id):
    if request.method=="PUT":
        category_name=request.data.get("category_name")
        u=blog_category.objects.filter(id=id)
        u.update(category_name=category_name)
        ser=blog_category_serialiser(u,many=True)
        return Response(ser.data)

@api_view(['POST'])
def add_blog(request):
    if request.method=="POST":
        blog_title=request.data.get("blog_title")
        blog_content=request.data.get("blog_content")
        blog_image
        # blog_cat
        # blog_comm





