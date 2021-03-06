# Generated by Django 2.2.7 on 2019-12-15 09:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=100)),
                ('community_desc', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('join_allowed', models.BooleanField(default=False)),
                ('newdt_allowed', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type_name', models.CharField(max_length=100)),
                ('data_type_desc', models.TextField(default='')),
                ('formfields', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Community')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(max_length=140)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roledesc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserBuilderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=100)),
                ('post_desc', models.TextField(default='')),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('post_data', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Community')),
                ('data_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.DataType')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserRole'),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(choices=[('IM', 'Image'), ('VI', 'Video'), ('AU', 'Audio'), ('TE', 'Text field'), ('TA', 'Text area'), ('UR', 'URI'), ('LO', 'Location'), ('DA', 'Date'), ('DE', 'Decimal'), ('IM', 'Integer')], default='TE', max_length=2)),
                ('field_label', models.CharField(max_length=50)),
                ('is_required', models.BooleanField(default=False)),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Community')),
            ],
        ),
        migrations.AddField(
            model_name='datatype',
            name='fields',
            field=models.ManyToManyField(to='polls.FormField'),
        ),
        migrations.AddField(
            model_name='datatype',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.MyUser'),
        ),
        migrations.CreateModel(
            name='CommunityTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_desc', models.CharField(max_length=100)),
                ('post', models.IntegerField()),
                ('tag_info', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Community')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=True)),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Community')),
                ('follower', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.MyUser'),
        ),
    ]
