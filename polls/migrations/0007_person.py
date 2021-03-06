# Generated by Django 3.2.6 on 2021-08-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
