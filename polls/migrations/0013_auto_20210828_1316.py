# Generated by Django 3.2.6 on 2021-08-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20210828_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='p_id',
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                      verbose_name='ID'),
            preserve_default=False,
        ),
    ]
