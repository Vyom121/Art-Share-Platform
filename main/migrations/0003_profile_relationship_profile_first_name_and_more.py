# Generated by Django 4.0.6 on 2022-07-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Relationship',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
