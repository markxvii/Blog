# Generated by Django user.0.5 on 2018-08-22 07:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_auto_20180822_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
