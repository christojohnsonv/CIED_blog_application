# Generated by Django 3.1.4 on 2021-12-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_remove_blog_blog_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='blog_o',
            field=models.ManyToManyField(through='blog_app.Blog_cat_relate', to='blog_app.Blog'),
        ),
    ]
