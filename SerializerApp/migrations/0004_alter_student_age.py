# Generated by Django 4.1.7 on 2023-04-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerializerApp', '0003_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
