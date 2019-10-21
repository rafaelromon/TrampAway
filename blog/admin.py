from django.contrib import admin
from django.db import models
# Register your models here.
from martor.widgets import AdminMartorWidget

from blog.models import Post, Author, Message


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'featured',)
    list_display = ('date', 'title', 'author', "featured")
    list_display_links = ('title',)
    ordering = ('-date',)
    readonly_fields = ('image_tag',)
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('founder',)
    list_display = ('user', 'founder',)
    list_display_links = ('user', 'founder')
    ordering = ('-user',)
    readonly_fields = ('image_tag',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email', 'read')
    list_display_links = ('name',)
    ordering = ('-date',)

    list_filter = ('read',)

    readonly_fields = ('date', 'name', 'email', 'message')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'name', 'email', 'parent_post')
    list_display_links = ('name',)
    ordering = ('-date_time',)

    list_filter = ('parent_post',)

    readonly_fields = ('date_time', 'name', 'email', 'comment', 'parent_post')


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Message, MessageAdmin)
