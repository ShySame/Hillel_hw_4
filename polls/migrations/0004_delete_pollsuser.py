# Generated by Django 3.2.6 on 2021-08-17 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_pollsuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PollsUser',
        ),
    ]
