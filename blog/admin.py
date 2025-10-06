from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    list_filter = ['created_at', 'author', 'categories']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    filter_horizontal = ['categories']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content', 'author__username', 'post__title']
    date_hierarchy = 'created_at'
