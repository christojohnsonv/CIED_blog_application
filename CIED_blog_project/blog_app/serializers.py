from django.db import models
from django.db.models import fields
from rest_framework import serializers
from blog_app.models import Category,Blog,Blog_cat_relate,blog_comment

class Category_serialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Blog_serialiser(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class Blog_cat_relate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_cat_relate
        fields='__all__'

class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = blog_comment
        fields='__all__'