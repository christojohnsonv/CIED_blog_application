from django.db import models
from django.db.models import fields
from rest_framework import serializers
from blog_app.models import User,blog_category,blog

class blog_category_serialiser(serializers.ModelSerializer):
    class Meta:
        model = blog_category
        fields = '__all__'

class blog_serialiser(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'

