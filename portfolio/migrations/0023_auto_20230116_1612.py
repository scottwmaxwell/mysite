# Generated by Django 3.2.9 on 2023-01-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20220823_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='skills_pics'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='date_acheived',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='certification',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='certification',
            name='image',
            field=models.ImageField(upload_to='certification_pics'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='certification',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='certification',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]