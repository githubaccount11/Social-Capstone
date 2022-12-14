# Generated by Django 4.1 on 2022-09-02 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text_content', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('subments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='capapp.comments')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.URLField(blank=True, max_length=1000, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('work', models.CharField(blank=True, max_length=50, null=True)),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, max_length=200, null=True)),
                ('date_joined', models.DateField(blank=True, max_length=200, null=True)),
                ('followed', models.ManyToManyField(blank=True, related_name='followed_profile', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends_profile', to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(blank=True, related_name='image_profile', to='capapp.images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField()),
                ('private', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
                ('profile_image', models.URLField(blank=True, max_length=1000, null=True)),
                ('text_content', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.URLField(blank=True, max_length=1000, null=True)),
                ('video', models.URLField(blank=True, max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Post', to='capapp.comments')),
            ],
        ),
    ]
