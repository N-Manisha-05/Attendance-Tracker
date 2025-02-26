from django import forms
from .models import Student,Faculty,Admin

from django.contrib.auth import get_user_model


class AddAdminForm(forms.ModelForm):
    # Add the fields here that are required in your admin table
    admin_id = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Admin  # Assuming you have an Admin model to handle these fields
        fields = ['admin_id', 'firstname', 'lastname', 'username', 'email', 'password', 'phone_number']

class DeleteAdminForm(forms.Form):
    admin_id = forms.ModelChoiceField(queryset=Admin.objects.all(), label="Select Admin to Delete")
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'firstname', 'lastname', 'email', 'password', 'phone_number', 
                  'parents_mobile_number', 'ssc_gpa', 'attendance_percentage']


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'firstname', 'lastname', 'email', 'password', 'phone_number', 'subject']


from django import forms
from .models import Faculty  # Ensure Faculty model is imported correctly

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty  # Link to the Faculty model
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'subject']  # Fields you want to update


from django import forms
from .models import Faculty

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'subject']  # Add all fields you want to be editable
