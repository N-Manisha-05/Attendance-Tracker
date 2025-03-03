# Generated by Django 5.1.3 on 2024-11-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(default="user", max_length=30, unique=True),
                ),
                (
                    "email",
                    models.EmailField(
                        default="user@example.com", max_length=254, unique=True
                    ),
                ),
                ("first_name", models.CharField(default="First Name", max_length=50)),
                ("last_name", models.CharField(default="Last Name", max_length=50)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default="0000000000", max_length=15, null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "admin_id",
                    models.CharField(
                        default="admin01",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("firstname", models.CharField(default="Sameera", max_length=100)),
                ("lastname", models.CharField(default="Madiledu", max_length=100)),
                (
                    "username",
                    models.CharField(default="msameera", max_length=100, unique=True),
                ),
                (
                    "email",
                    models.EmailField(
                        default="sameera@gmail.com", max_length=254, unique=True
                    ),
                ),
                ("password", models.CharField(default="sammu@123", max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default="1234567890", max_length=15, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "faculty_id",
                    models.CharField(
                        default="faculty01",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("firstname", models.CharField(default="Alice", max_length=100)),
                ("lastname", models.CharField(default="Smith", max_length=100)),
                (
                    "email",
                    models.EmailField(
                        default="faculty01@example.com", max_length=254, unique=True
                    ),
                ),
                ("password", models.CharField(default="faculty123", max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default="9876543210", max_length=15, null=True
                    ),
                ),
                ("subject", models.CharField(default="Mathematics", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "student_id",
                    models.CharField(
                        default="student01",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("firstname", models.CharField(default="John", max_length=100)),
                ("lastname", models.CharField(default="Doe", max_length=100)),
                (
                    "email",
                    models.EmailField(
                        default="student01@example.com", max_length=254, unique=True
                    ),
                ),
                (
                    "password",
                    models.CharField(default="studentpass123", max_length=255),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default="1234567890", max_length=15, null=True
                    ),
                ),
                (
                    "parents_mobile_number",
                    models.CharField(
                        blank=True, default="9876543210", max_length=15, null=True
                    ),
                ),
                ("ssc_gpa", models.FloatField(default=3.5)),
                ("attendance_percentage", models.FloatField(default=80.0)),
            ],
        ),
    ]
