# Generated by Django 5.0.1 on 2024-11-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0003_alter_admin_admin_id_alter_admin_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="attendance_percentage",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
