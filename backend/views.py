from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Admin,Faculty,Student
from django.contrib.auth.hashers import check_password
from .forms import StudentForm, FacultyForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from .forms import AddAdminForm, DeleteAdminForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import Student ,Faculty  # Import your Student model

# Admin = get_user_model()


def add_admin(request):
   
    if request.method == 'POST':
        form = AddAdminForm(request.POST)
        if form.is_valid():
            # form.save()
            admin = form.save(commit=False)
            # Optionally hash the password before saving
            admin.password = make_password(form.cleaned_data['password'])
            admin.save()
            messages.success(request, 'New admin added successfully!')
            return redirect('administration_dashboard')
    else:
        form = AddAdminForm()
    return render(request, 'backend/add_admin.html', {'form': form})


def delete_admin(request):
    
    if request.method == 'POST':
        form = DeleteAdminForm(request.POST)
        if form.is_valid():
            admin = form.cleaned_data['admin_id']
            admin.delete()
            messages.success(request, 'Admin deleted successfully!')
            return redirect('administration_dashboard')
    else:
        form = DeleteAdminForm()
    return render(request, 'backend/delete_admin.html', {'form': form})
def home(request):
    return render(request, 'backend/home.html')




def faculty_login(request):
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty_id')
        password = request.POST.get('password')
        
        try:
            # Attempt to find the faculty by faculty_id
            faculty = Faculty.objects.get(faculty_id=faculty_id)
            
            # Check password
            if faculty.password == password:  # Plain text password check
                request.session['faculty_id'] = faculty.faculty_id  # Store session
                return redirect('faculty_dashboard')  # Redirect to home page
            else:
                messages.error(request, 'Invalid faculty ID or password')
        except Faculty.DoesNotExist:
            messages.error(request, 'Faculty ID does not exist.')

    return render(request, 'backend/faculty_login.html')



def administration_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            # Fetch the admin by username
            admin = Admin.objects.get(username=username)
            
            # Check if the provided password matches the admin's password
            if check_password(password, admin.password):
                # Log the admin in by attaching the admin object to the session
                request.session['admin_id'] = admin.admin_id
                messages.success(request, "Login successful!")
                return redirect('administration_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        except Admin.DoesNotExist:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'backend/administration_login.html')

def administration_logout(request):
    if 'admin_id' in request.session:
        del request.session['admin_id']
    
    # Redirect to the home page after logout
    return redirect('home')

#@login_required
def administration_dashboard(request):
    # Check if the user is logged in by confirming the presence of 'admin_id' in the session
    if 'admin_id' not in request.session:
        messages.error(request, "You must be logged in to access the admin dashboard.")
        return redirect('administration_login')
    
    return render(request, 'backend/administration_dashboard.html')

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
import logging


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        
        # Check if student with the same student_id already exists
        student_id = request.POST.get('student_id')
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "A student with this Student ID already exists.")
            return render(request, 'backend/add_student.html', {'form': form})

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('administration_dashboard')
        else:
            messages.error(request, "Form submission failed. Please check the fields.")
    else:
        form = StudentForm()

    return render(request, 'backend/add_student.html', {'form': form})

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty member added successfully!")
            return redirect('administration_dashboard')
    else:
        form = FacultyForm()
    return render(request, 'backend/add_faculty.html', {'form': form})



def view_student(request):
    students = Student.objects.all()
    return render(request, 'backend/view_student.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(student_id=student_id)
    return render(request, 'backend/student_detail.html', {'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('view_student')



def view_faculty(request):
    faculty_members = Faculty.objects.all()
    return render(request, 'backend/view_faculty.html', {'faculty_members': faculty_members})

def faculty_detail(request, faculty_id):
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    return render(request, 'backend/faculty_detail.html', {'faculty': faculty})

def delete_faculty(request, faculty_id):
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    faculty.delete()
    messages.success(request, "Faculty deleted successfully!")
    return redirect('view_faculty')


from .models import  Attendance
from django.http import HttpResponse




from datetime import datetime
from django.http import JsonResponse



from django.http import JsonResponse
from datetime import datetime
from .models import Attendance
import json  # Import json to parse incoming AJAX request data
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Student  # Ensure the correct model is imported


import json
from django.http import JsonResponse
from .models import Attendance  # Assuming you have an Attendance model

def mark_attendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('student_id')
            status = data.get('status')
            subject_name = data.get('subject_name')
            attendance_date = data.get('attendance_date')  # Get the date from the request

            # Validate if the date was received
            if not attendance_date:
                return JsonResponse({'success': False, 'error': 'Attendance date not provided.'})
            
            # Save attendance in the database
            Attendance.objects.create(
                student_id=student_id,
                status=status,
                subject_name=subject_name,
                attendance_date=attendance_date  # Save the provided date, not the current date
            )

            return JsonResponse({'success': True, 'status': status})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


from datetime import date
from django.shortcuts import render
from .models import Faculty, Student

def faculty_dashboard(request):
    # Fetch logged-in faculty details
    faculty_id = request.session.get('faculty_id')
    faculty = Faculty.objects.get(faculty_id=faculty_id)

    # Fetch all students
    students = Student.objects.all()

    # Get current date
    current_date = date.today().strftime('%Y-%m-%d')

    context = {
        'faculty_details': {
            'faculty_id': faculty.faculty_id,
            'firstname': faculty.firstname,
            'lastname': faculty.lastname,
            'email': faculty.email,
            'phone_number': faculty.phone_number,
            'subject': faculty.subject,
        },
        'students': students,
        'current_date': current_date,
    }

    return render(request, 'backend/faculty_dashboard.html', context)


from django.shortcuts import render, redirect
from .models import Faculty
from django.contrib import messages

def update_faculty_profile(request, faculty_id):
    faculty = Faculty.objects.get(faculty_id=faculty_id)

    if request.method == 'POST':
        faculty.firstname = request.POST.get('firstname', faculty.firstname)
        faculty.lastname = request.POST.get('lastname', faculty.lastname)
        faculty.email = request.POST.get('email', faculty.email)
        faculty.phone_number = request.POST.get('phone_number', faculty.phone_number)
        faculty.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('faculty_dashboard')

    return render(request, 'backend/update_faculty_profile.html', {'faculty': faculty})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty  # Assuming Faculty is your model name
from .forms import FacultyProfileForm  # Assuming you have a form for the faculty profile update

def faculty_profile_view(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    
    if request.method == 'POST':
        form = FacultyProfileForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')  # Redirect to dashboard after successful update
    else:
        form = FacultyProfileForm(instance=faculty)
    
    context = {'form': form, 'faculty': faculty}
    return render(request, 'faculty_profile.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty
from .forms import FacultyProfileForm  # Assuming you have a form for updating the faculty profile




from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty
from .forms import FacultyProfileForm  # Assuming you have a form for updating the faculty profile




from django.db.models import Count, Case, When, F
from backend.models import Student, Attendance

def calculate_attendance_percentage(request):
    # Step 1: Get the count of "Present" and total attendance for each student
    attendance_stats = Attendance.objects.values('student_id').annotate(
        total_classes=Count('id'),
        total_present=Count(Case(When(status='Present', then=1)))
    )

    # Step 2: Loop through the results to calculate percentage and update the student table
    for stats in attendance_stats:
        student_id = stats['student_id']
        total_classes = stats['total_classes']
        total_present = stats['total_present']
        
        # Avoid division by zero
        if total_classes > 0:
            attendance_percentage = (total_present / total_classes) * 100
        else:
            attendance_percentage = 0
        
        # Update the student table with the calculated percentage
        Student.objects.filter(student_id=student_id).update(attendance_percentage=attendance_percentage)
    update_low_attendance()
    return JsonResponse({'success': True, 'message': 'Attendance percentage calculated and updated successfully.'})


from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Student, LowAttendance




def update_low_attendance():
    low_attendance_students = Student.objects.filter(attendance_percentage__lt=75)
    print("Low attendance students:", low_attendance_students)  # Debugging line

    for student in low_attendance_students:
        if not LowAttendance.objects.filter(student=student).exists():
            LowAttendance.objects.create(
                student=student,
                attendance_percentage=student.attendance_percentage,
            )
            

# View to handle low attendance students
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Student, LowAttendance  # Ensure these are the correct models
import logging
from django.core.paginator import Paginator
from django.core.mail import send_mail, send_mass_mail
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student, LowAttendance

# Set up logging
logger = logging.getLogger(__name__)

from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Student, LowAttendance
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student, LowAttendance
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Student
from smtplib import SMTPAuthenticationError
from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Student, LowAttendance
def low_attendance_students(request):
    # Step 1: Populate LowAttendance table with students having attendance < 75%
    low_attendance_students = Student.objects.filter(attendance_percentage__lt=75)
    LowAttendance.objects.all().delete()  # Clear previous data
    LowAttendance.objects.bulk_create(
        [LowAttendance(student=student, attendance_percentage=student.attendance_percentage) 
         for student in low_attendance_students]
    )
    
    # Step 2: Fetch students from LowAttendance table
    students = LowAttendance.objects.select_related('student').all()

    # Step 3: Pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Step 4: Check if there are students with low attendance
    if not page_obj.object_list:
        return render(request, 'backend/low_attendance.html', {'message': 'No students with low attendance at the moment.'})

    # Step 5: Handle POST request for sending emails
    if request.method == 'POST':
        student_ids = request.POST.getlist('students')
        emails=[]
        subject = "Alert: Low Attendance"
        # message = "Your attendance has fallen below 75%. Please ensure to attend classes regularly."
        
        for student_id in student_ids:
            student = Student.objects.get(student_id=student_id)
            message = (
                subject,
                f"Dear {student.firstname},\n\nYour attendance is  {student.attendance_percentage} and it is  below 75%. Please ensure to attend classes regularly.You cant attend exams unless you improve your atendance.",
                'attendancemanagement7@gmail.com',
                [student.email]
            )
            # send_mail(subject, message, 'attendancemanagement7@gmail.com', [student.email])
            emails.append(message)
        send_mass_mail(tuple(emails))
        # return JsonResponse({'status': 'Email sent to selected students'})
        return render(request, 'backend/low_attendance.html', {
            'students': page_obj.object_list,
            'page_obj': page_obj,
            'success_message': 'Emails sent successfully!'
        })
        print("Mail sent successfully!")

    # Step 6: Render the low attendance page
    return render(request, 'backend/low_attendance.html', {
        'students': page_obj.object_list,
        'page_obj': page_obj,
       
        # 'message': request.GET.get('message', '')
    })


from django.core.mail import send_mail
from django.conf import settings


def student_login(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        
        try:
            # Lookup by student_id in backend_student
            student = Student.objects.get(student_id=student_id)
            
            # Check if the provided password matches
            if student.password == password:  # Plain text password check
                request.session['student_id'] = student.student_id  # Store session
                return redirect('student_dashboard')  # Redirect to the home page
            else:
                messages.error(request, 'Invalid student ID or password')
        except Student.DoesNotExist:
            messages.error(request, 'You dont have access to login')

    return render(request, 'backend/student_login.html')


def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(student_id=student_id)
    return render(request, 'backend/student_dashboard.html', {'student': student})

def update_profile(request):
    student_id = request.session.get('student_id')
    firstname=request.session.get('firstname')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(student_id=student_id)

    if request.method == 'POST':
        student.lastname = request.POST['lastname']
        student.email = request.POST['email']
        student.phone_number = request.POST['phone_number']
        student.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('student_dashboard')

    return render(request, 'backend/update_profile.html', {'student': student})


def faculty_profile(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        messages.error(request, "You are not logged in!")
        return redirect('faculty_login')

    # faculty = Faculty.objects.filter(faculty_id=faculty_id).first()
    faculty = get_object_or_404(Faculty, faculty_id=faculty_id)
    return render(request, 'backend/faculty_profile.html', {'faculty': faculty})
    if not faculty:
        messages.error(request, "Faculty not found.")
        return redirect('faculty_login')

    return render(request, 'backend/faculty_profile.html', {'faculty': faculty})

def update_faculty_profile(request, faculty_id):
    faculty = get_object_or_404(Faculty, faculty_id=faculty_id)

    if request.method == 'POST':
        # Update faculty details
        faculty.firstname = request.POST['firstname']
        faculty.lastname = request.POST['lastname']
        faculty.email = request.POST['email']
        faculty.phone_number = request.POST.get('phone_number', '')
        faculty.subject = request.POST['subject']

        # Update password only if provided
        if request.POST.get('password'):
            faculty.password = request.POST['password']

        faculty.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('faculty_profile')

    return render(request, 'backend/update_faculty_profile.html', {'faculty': faculty})