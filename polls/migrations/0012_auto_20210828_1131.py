# Generated by Django 3.2.6 on 2021-08-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='p_id',
        ),
        migrations.AddField(
            model_name='log',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True,
                                      serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]