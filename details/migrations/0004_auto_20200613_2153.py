# Generated by Django 3.0.7 on 2020-06-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20200613_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiview',
            old_name='stu_email',
            new_name='stu_age',
        ),
    ]