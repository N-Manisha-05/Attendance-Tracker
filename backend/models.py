from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# User Manager to handle user creation and superuser creation
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    student_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

# Admin Model
class Admin(models.Model):
    admin_id = models.CharField(max_length=50, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# Student Model
class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    parents_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    ssc_gpa = models.FloatField()
    attendance_percentage = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# Faculty Model
class Faculty(models.Model):
    faculty_id = models.CharField(max_length=50, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.faculty_id})"

class LowAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_percentage = models.FloatField()
    alert_sent = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.student.firstname} {self.student.lastname} - {self.attendance_percentage}%"

from .models import Student  # Assuming the Student model is in the same app



# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Link to Student model
#     subject_name = models.CharField(max_length=100,  choices=[('present', 'Present'), ('absent', 'Absent')],
#         default='absent')  # Name of the subject
#     date = models.DateField(null=True, blank=True)  # Date of the attendance
#     # status = models.BooleanField()  # True for present, False for absent
#     PRESENT = 'present'
#     ABSENT = 'absent'
#     ATTENDANCE_STATUS_CHOICES = [
#         (PRESENT, 'Present'),
#         (ABSENT, 'Absent'),
#     ]
#     status = models.CharField(max_length=7, choices=ATTENDANCE_STATUS_CHOICES)
#     def __str__(self):
#         return f"{self.student.firstname} {self.student.lastname} - {self.subject_name} ({'Present' if self.status else 'Absent'})"

import datetime
from django.db import models
from backend.models import Student, Faculty  # Import Student and Faculty models

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Link to student
    subject_name = models.CharField(max_length=100)  # Subject for the attendance
    attendance_date = models.DateField(default=datetime.date.today)  # Date when attendance is marked
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])  # Status of attendance

    def __str__(self):
        return f"{self.student.firstname} - {self.subject_name} - {self.date} - {self.status}"
