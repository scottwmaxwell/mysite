# Generated by Django 3.2.9 on 2023-01-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20230117_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured',
            field=models.BooleanField(unique=True),
        ),
    ]
