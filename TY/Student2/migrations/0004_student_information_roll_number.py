# Generated by Django 3.2.7 on 2021-12-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student2', '0003_auto_20211202_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_information',
            name='roll_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
