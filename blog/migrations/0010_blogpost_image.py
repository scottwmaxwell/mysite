# Generated by Django 3.2.9 on 2023-01-17 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='blogposts'),
        ),
    ]
