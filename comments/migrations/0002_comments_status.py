# Generated by Django 3.0.3 on 2020-03-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
