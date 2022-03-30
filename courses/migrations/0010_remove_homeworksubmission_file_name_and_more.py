# Generated by Django 4.0.2 on 2022-03-30 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_homework_instruction_alter_homework_due_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworksubmission',
            name='file_name',
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_time',
            field=models.CharField(default=datetime.datetime(2022, 4, 2, 22, 16, 15, 330364), max_length=200),
        ),
        migrations.AlterField(
            model_name='homeworksubmission',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homeworksubmission',
            name='marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homeworksubmission',
            name='submission_time',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 3, 30, 22, 16, 15, 331363), max_length=200, null=True),
        ),
    ]
