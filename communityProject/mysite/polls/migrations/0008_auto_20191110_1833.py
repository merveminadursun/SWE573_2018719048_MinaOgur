# Generated by Django 2.2.7 on 2019-11-10 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20191110_1831'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Community_Follower',
            new_name='CommunityFollower',
        ),
        migrations.RenameModel(
            old_name='Community_Tag',
            new_name='CommunityTag',
        ),
        migrations.RenameModel(
            old_name='Data_Type',
            new_name='DataType',
        ),
        migrations.RenameModel(
            old_name='Form_Field',
            new_name='FormField',
        ),
        migrations.RenameModel(
            old_name='User_Builder_Req',
            new_name='UserBuilderRequest',
        ),
        migrations.RenameModel(
            old_name='UserRoles',
            new_name='UserRole',
        ),
    ]