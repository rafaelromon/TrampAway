from django.contrib import admin
from django.db import models
# Register your models here.
from martor.widgets import AdminMartorWidget

from blog.models import Post, Author, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('date', 'title', 'author')
    list_display_links = ('title',)
    ordering = ('-date',)
    readonly_fields = ('image_tag',)
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    ordering = ('-user',)
    readonly_fields = ('image_tag',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email', 'read')
    list_display_links = ('name',)
    ordering = ('-date',)

    list_filter = ('read',)

    readonly_fields = ('date', 'name', 'email', 'message')


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
