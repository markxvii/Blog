# Generated by Django user.0.5 on 2018-08-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0004_auto_20180822_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
