# Generated by Django 4.2.7 on 2023-11-05 12:05

from django.db import migrations, models
import functools
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uploadimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimages',
            name='image',
            field=models.ImageField(upload_to=functools.partial(main_app.models.make_file_path, *('image',), **{})),
        ),
    ]