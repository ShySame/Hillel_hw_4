# Generated by Django 3.2.6 on 2021-08-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20210828_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
