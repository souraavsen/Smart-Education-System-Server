# Generated by Django 4.0.2 on 2022-03-30 23:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('details', models.TextField()),
                ('links', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Home Work', max_length=100)),
                ('instruction', models.CharField(blank=True, max_length=300)),
                ('question', models.TextField()),
                ('total_marks', models.FloatField()),
                ('due_time', models.CharField(default=datetime.datetime(2022, 4, 3, 5, 50, 57, 396848), max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/HomeworksQuestions')),
                ('course_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursecontent')),
            ],
        ),
        migrations.CreateModel(
            name='JoinClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.classes')),
                ('students', models.ManyToManyField(to='accounts.StudentPorfile')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWorkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_time', models.CharField(blank=True, max_length=200, null=True)),
                ('submitted_file', models.FileField(blank=True, upload_to='media/Homeworks')),
                ('answer', models.TextField(blank=True, null=True)),
                ('marks', models.CharField(blank=True, max_length=10, null=True)),
                ('homework_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentporfile')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('course_code', models.CharField(max_length=100)),
                ('classes', models.ManyToManyField(to='courses.JoinClasses')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherporfile')),
            ],
        ),
        migrations.CreateModel(
            name='CourseContentVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('video_link', models.TextField()),
                ('course_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursecontent')),
            ],
        ),
        migrations.CreateModel(
            name='CourseContentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Content files', max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('course_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursecontent')),
            ],
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses'),
        ),
    ]
