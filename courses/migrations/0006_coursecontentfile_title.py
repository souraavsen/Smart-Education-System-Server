# Generated by Django 4.0.2 on 2022-03-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_coursecontent_coursecontentfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontentfile',
            name='title',
            field=models.CharField(default='Content Link', max_length=200),
        ),
    ]