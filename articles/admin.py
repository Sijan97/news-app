from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.TabularInline):
    """Pass Comment as model."""
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    """Display all commetns to the post."""
    inlines = [
        CommentInLine,
        ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)