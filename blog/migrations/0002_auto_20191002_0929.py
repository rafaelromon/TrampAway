# Generated by Django 2.2.6 on 2019-10-02 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('title', models.CharField(max_length=124, verbose_name='title')),
                ('subtitle', models.CharField(max_length=124, verbose_name='subtitle')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='header image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]