# Generated by Django 4.1 on 2022-09-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capapp', '0016_remove_comments_subments_remove_post_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='private',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
