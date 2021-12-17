from django.contrib import admin
from.models import Category,Blog,Blog_cat_relate,blog_comment

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Blog_cat_relate)
admin.site.register(blog_comment)

