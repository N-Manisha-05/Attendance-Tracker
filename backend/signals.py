from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.models import Attendance, Student
from django.db.models import Count, Case, When

@receiver(post_save, sender=Attendance)
def update_attendance_percentage(sender, instance, **kwargs):
    """ Automatically updates the attendance percentage when an attendance record is created or updated. """
    student_id = instance.student_id

    # Step 1: Calculate total classes and total presents for the specific student
    attendance_stats = Attendance.objects.filter(student_id=student_id).aggregate(
        total_classes=Count('id'),
        total_present=Count(Case(When(status='Present', then=1)))
    )

    total_classes = attendance_stats['total_classes']
    total_present = attendance_stats['total_present']

    # Step 2: Calculate the attendance percentage (avoid division by zero)
    if total_classes > 0:
        attendance_percentage = (total_present / total_classes) * 100
    else:
        attendance_percentage = 0

    # Step 3: Update the `attendance_percentage` field in the Student table
    Student.objects.filter(student_id=student_id).update(attendance_percentage=attendance_percentage)

