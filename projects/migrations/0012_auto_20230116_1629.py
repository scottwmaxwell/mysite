# Generated by Django 3.2.9 on 2023-01-16 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_chrome_extension_update_xml_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='chrome_extension',
        ),
        migrations.DeleteModel(
            name='chrome_extension_update',
        ),
    ]