# Generated by Django 4.0.6 on 2022-07-23 14:52

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
