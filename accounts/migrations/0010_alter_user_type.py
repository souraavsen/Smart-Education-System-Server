# Generated by Django 4.0.2 on 2022-03-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], max_length=100),
        ),
    ]
