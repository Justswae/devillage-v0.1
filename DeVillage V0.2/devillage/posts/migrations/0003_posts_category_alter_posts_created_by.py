# Generated by Django 4.1.1 on 2023-08-10 22:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_posts_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.category'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_by',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]