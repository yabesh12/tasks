# Generated by Django 3.0.7 on 2020-06-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiview',
            name='stu_class',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='apiview',
            name='stu_email',
            field=models.IntegerField(null=True),
        ),
    ]
