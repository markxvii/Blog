# Generated by Django user.0.5 on 2018-08-18 04:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-last_update_time']},
        ),
    ]
