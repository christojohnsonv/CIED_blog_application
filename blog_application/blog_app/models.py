from os import truncate
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.deletion import CASCADE,SET_NULL,SET_DEFAULT

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    username=models.CharField(max_length=100,null=True,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['role','phone']
    objects=UserManager()

    def get_username(self):
        return self.email

class blog_category(models.Model):
    category_name=models.CharField(default="Null category Name",max_length=20,null=False)

class blog_comment(models.Model):
    comment_content=models.CharField(max_length=40,null=True)
    comment_email=models.EmailField(max_length=20,null=True)

class blog(models.Model):
    blog_title=models.CharField(max_length=40,null=True,blank=True)
    blog_content=models.CharField(max_length=10000,null=True,blank=True)
    blog_image=models.ImageField(upload_to='images/',null=True,blank=True)
    blog_cat=models.ManyToManyField(blog_category,null=True,blank=True)
    blog_comm=models.ForeignKey(blog_comment,on_delete=SET_NULL,null=True,blank=True)


