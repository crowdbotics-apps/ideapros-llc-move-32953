# Generated by Django 2.2.28 on 2022-07-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]