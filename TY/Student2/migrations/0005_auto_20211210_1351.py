# Generated by Django 3.2.7 on 2021-12-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student2', '0004_student_information_roll_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_information',
            name='DBMS',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_information',
            name='OS',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_information',
            name='Python',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_information',
            name='TOC',
            field=models.CharField(default=10, max_length=30),
            preserve_default=False,
        ),
    ]
