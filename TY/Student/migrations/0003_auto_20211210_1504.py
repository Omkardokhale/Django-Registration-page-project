# Generated by Django 3.2.7 on 2021-12-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20211129_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_information',
            old_name='username',
            new_name='reg_number',
        ),
        migrations.RemoveField(
            model_name='student_information',
            name='email',
        ),
        migrations.AddField(
            model_name='student_information',
            name='DBMS',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_information',
            name='OS',
            field=models.CharField(default=10, max_length=30),
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
        migrations.AddField(
            model_name='student_information',
            name='roll_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
