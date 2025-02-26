from django.contrib import admin
from .models import Admin, Student, Faculty

# Register models using the @admin.register decorator to avoid duplicate registration
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'firstname', 'lastname', 'username', 'email', 'phone_number')

# Register the Student and Faculty models as usual
admin.site.register(Student)
admin.site.register(Faculty)
