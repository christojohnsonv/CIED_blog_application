# Generated by Django 3.1.4 on 2021-12-16 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_category_blog_o'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_email', models.EmailField(max_length=20, null=True)),
                ('comment_content', models.CharField(max_length=300, null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.blog')),
            ],
        ),
    ]