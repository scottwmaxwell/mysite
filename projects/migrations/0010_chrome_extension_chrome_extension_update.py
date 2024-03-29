# Generated by Django 3.2.9 on 2022-10-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='chrome_extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('file', models.FileField(blank=True, upload_to='application')),
            ],
        ),
        migrations.CreateModel(
            name='chrome_extension_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('xml_file', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
