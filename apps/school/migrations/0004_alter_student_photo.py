# Generated by Django 4.2.2 on 2023-06-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_alter_class_student_alter_school_classrooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="student_photos/"),
        ),
    ]
