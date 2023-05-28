from django.contrib import admin
from .models import Category, Post, Like


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('img_cat' ,'cat_id', 'title', 'description', 'cat_url', 'cat_created_at')
    search_fields  = ('cat_id', 'title', 'cat_url')
    list_filter = ('cat_id', 'title', 'cat_url')


class PostAdmin(admin.ModelAdmin):
    list_display = ('img_post' ,'post_id', 'title', 'post_url', 'category_name', 'post_author', 'post_created_at' )
    search_fields = ('post_id', 'title', 'post_url', 'category_name')
    list_filter = ('post_id', 'title', 'post_url', 'category_name')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user' , 'post', 'created_at') 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)