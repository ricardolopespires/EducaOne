# Generated by Django 4.1.3 on 2023-05-11 17:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
