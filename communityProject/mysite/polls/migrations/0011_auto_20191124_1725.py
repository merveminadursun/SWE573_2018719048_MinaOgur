# Generated by Django 2.2.7 on 2019-11-24 14:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20191117_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitytag',
            name='tag_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='formfields',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
    ]
