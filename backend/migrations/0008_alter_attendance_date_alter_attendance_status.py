# Generated by Django 5.0.7 on 2024-12-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0007_rename_attendance_date_attendance_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="status",
            field=models.CharField(
                choices=[("present", "Present"), ("absent", "Absent")], max_length=7
            ),
        ),
    ]
