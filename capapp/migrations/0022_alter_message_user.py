# Generated by Django 4.1 on 2022-09-28 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capapp', '0021_rename_user_chat_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=516, on_delete=django.db.models.deletion.PROTECT, related_name='user_message', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]