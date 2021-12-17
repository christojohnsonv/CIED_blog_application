from django.db import models
from django.db.models.deletion import CASCADE,SET_NULL,SET_DEFAULT


class Blog(models.Model):
    blog_title=models.CharField(max_length=40,null=True,blank=True)
    blog_content=models.CharField(max_length=10000,null=True,blank=True)
    blog_image=models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return self.blog_title

class Category(models.Model):
    category_name=models.CharField(max_length=20)
    blog_o=models.ManyToManyField(Blog,through="Blog_cat_relate")
    def __str__(self):
        return self.category_name

class Blog_cat_relate(models.Model):
    blog=models.ForeignKey(Blog,on_delete=CASCADE)
    category=models.ForeignKey(Category,on_delete=CASCADE)

    class Meta:
        unique_together = [['blog','category']]
    
    def __str__(self):
        return '%s - %s ' % (self.blog.blog_title,self.category.category_name)

class blog_comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=CASCADE,related_name="comments",null=True)
    comment_email=models.EmailField(max_length=50,null=True)
    comment_content=models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return '%s - %s' % (self.blog.blog_title,self.comment_email)
    
    
