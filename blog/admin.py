from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
from martor.widgets import AdminMartorWidget
from django.db import models

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('date', 'title', 'author')
    list_display_links = ('title',)
    ordering = ('-date',)
    readonly_fields = ('image_tag',)
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post, MarkdownxModelAdmin)
