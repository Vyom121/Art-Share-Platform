# Generated by Django 4.0.6 on 2022-07-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_profile_bgimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bgimage',
            field=models.ImageField(default='bg.jpg', upload_to='bg_image'),
        ),
    ]
