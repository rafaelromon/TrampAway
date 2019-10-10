import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from martor.models import MartorField


class Post(models.Model):
    date = models.DateField(default=datetime.date.today, verbose_name=_("date"))
    title = models.CharField(max_length=124, verbose_name=_("title"))
    subtitle = models.CharField(max_length=124, verbose_name=_("subtitle"))
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("author"))
    text = MartorField(blank=True, verbose_name=_("text"))

    header_image = models.ImageField(null=True, blank=True, upload_to="articles", verbose_name=_("header image"))

    def image_tag(self):
        return mark_safe('<img src="%s" height="150"/>' % self.header_image.url)

    image_tag.short_description = _('Header Image')
    image_tag.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)