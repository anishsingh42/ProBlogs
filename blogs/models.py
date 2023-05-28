from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = HTMLField()
    cat_created_at = models.DateField(auto_now_add=True)
    
    cat_url = models.CharField(max_length=200) #unique id for the page to locate
    image_cat = models.ImageField(upload_to='category/', default = 'category/default_img.jpg')

    def __str__(self):
        return self.title
    
    def img_cat(self):
        return format_html('<img src = "{}" style = "width:50px; height:50px; border-radius:50%;">' .format(self.image_cat.url))
    
class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    post_url = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='blogs_post')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_post = models.ImageField(upload_to='post/')
    post_author = models.CharField(max_length=100, default='Admin')
    post_created_at = models.DateField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def img_post(self):
        return format_html('<img src = "{}" style = "width:50px; height:50px; border-radius:50%;">' .format(self.image_post.url))

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username