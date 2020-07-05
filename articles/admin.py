from django.contrib import admin
from .models import Article, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


admin.site.register(Comment)
