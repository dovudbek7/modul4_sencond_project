# blog/admin.py
from django.contrib import admin
from .models import Article, MultimediaContent, Comment


# Custom admin for Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "article_type", "author", "created_at")
    list_filter = ("article_type", "author")
    search_fields = ("title", "author")


# Custom admin for Multimedia Content
@admin.register(MultimediaContent)
class MultimediaContentAdmin(admin.ModelAdmin):
    list_display = ("title", "content_type", "uploaded_at")
    list_filter = ("content_type",)
    search_fields = ("title",)


# Custom admin for Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "article", "is_approved", "created_at")
    list_filter = ("is_approved", "article")
    search_fields = ("content", "author")
