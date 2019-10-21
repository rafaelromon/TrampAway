import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from martor.models import MartorField
from martor.utils import markdownify


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("user"))
    description = models.TextField(verbose_name=_("description"))

    founder = models.BooleanField(default=False, verbose_name=_("founder"))

    profile_picture = models.ImageField(null=True, blank=True, upload_to="authors", verbose_name=_("header image"))

    def image_tag(self):
        return mark_safe('<img src="%s" height="150"/>' % self.profile_picture.url)

    image_tag.short_description = _('Profile Picture')
    image_tag.allow_tags = True

    class Meta:
        ordering = ['-user']
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()


class Message(models.Model):
    date = models.DateField(default=datetime.date.today, verbose_name=_("date"))
    name = models.CharField(max_length=124, verbose_name=_("name"))
    email = models.CharField(max_length=124, verbose_name=_("email"))

    read = models.BooleanField(default=False, verbose_name=_("read"))

    message = models.TextField(verbose_name=_("message"))

    class Meta:
        ordering = ['-date']
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.name


class Post(models.Model):
    date = models.DateField(default=datetime.date.today, verbose_name=_("date"))
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name=_("author"))

    title = models.CharField(max_length=124, verbose_name=_("title"))
    subtitle = models.CharField(max_length=124, verbose_name=_("subtitle"))

    featured = models.BooleanField(default=False, verbose_name=_("featured"))

    header_image = models.ImageField(null=True, blank=True, upload_to="articles", verbose_name=_("header image"))

    def image_tag(self):
        return mark_safe('<img src="%s" height="150"/>' % self.header_image.url)

    image_tag.short_description = _('Header Image')
    image_tag.allow_tags = True

    text = MartorField(blank=True, verbose_name=_("text"))

    class Meta:
        ordering = ['-date']
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    @property
    def formatted_markdown(self):
        return markdownify(self.text)


class Comment(models.Model):
    date_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=_("date_time"))
    name = models.CharField(max_length=124, verbose_name=_("name"))
    email = models.CharField(max_length=124, verbose_name=_("email"))

    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("parent_post"))

    comment = models.TextField(verbose_name=_("comment"))

    class Meta:
        ordering = ['-date_time']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name
