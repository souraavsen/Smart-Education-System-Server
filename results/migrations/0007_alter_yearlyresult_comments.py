# Generated by Django 4.0.2 on 2022-03-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_alter_yearlyresult_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlyresult',
            name='comments',
            field=models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Bellow Average', 'Bellow Average'), ('Poor', 'Poor'), ('Average', 'Average'), ('Very Good', 'Very Good'), ('Good', 'Good')], max_length=50, null=True),
        ),
    ]