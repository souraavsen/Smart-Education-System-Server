# Generated by Django 4.0.2 on 2022-03-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_teacherporfile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=100),
        ),
    ]