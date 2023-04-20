# Generated by Django 3.2.18 on 2023-04-20 00:49

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='select1_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='select_image'),
        ),
        migrations.AddField(
            model_name='post',
            name='select2_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='select_image'),
        ),
    ]