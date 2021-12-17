from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def get_blog_bycat(request):
    cat=request.data.get("cat")
    if cat:
        if Category.objects.filter(id=cat).exists():
            cat=Category.objects.get(id=cat)
            g=cat.blog_o.all()
            ser=Blog_serialiser(g,many=True)
            return Response(ser.data)
        else:
            return Response("category Not Found")
    else:
        g=Blog.objects.all()
        ser=Blog_serialiser(g,many=True)
        return Response(ser.data)
        

@api_view(['POST'])
def post_comment(request,id):
    if Blog.objects.filter(id=id).exists():
        if request.method=="POST":
            comment_email=request.data.get("comment_email")
            if comment_email:
                comment_content=request.data.get("comment_content")
                post_c=Blog.objects.get(id=id)
                blog_comment.objects.create(blog=post_c,comment_email=comment_email,comment_content=comment_content)
                return Response("Comment Created")
            else:
                return Response("Comments can only be post with an email id")
    else:
        return Response("Blog Not Found")



@api_view(['GET'])
def get_blogbyid(request,id):
    if Blog.objects.filter(id=id).exists():
        g=Blog.objects.filter(id=id)
        ser=Blog_serialiser(g,many=True)
        b=ser.data
        for i in b:
            comm=blog_comment.objects.filter(blog=i['id'])
            if comm:
                c_ser=comment_serializer(blog_comment.objects.filter(blog=i['id']),many=True)
                i.update({"comments":c_ser.data})
        return Response(ser.data)
    else:
        return Response("No Blog Found")