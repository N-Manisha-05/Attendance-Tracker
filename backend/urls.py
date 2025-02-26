from django.urls import path
from . import views
from django.urls import path
from backend.views import calculate_attendance_percentage
urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('home/', views.home, name='home'),  # Ensure this is for the home page
    path('login/', views.administration_login, name='administration_login'),  # Admin login page
   
    path('student/login/', views.student_login, name='student_login'),  # Student login page
  
    path('faculty/login/', views.faculty_login, name='faculty_login'),  # Faculty login page
    
    path('dashboard/', views.administration_dashboard, name='administration_dashboard'),  # Admin dashboard view
    path('logout/', views.administration_logout, name='administration_logout'),


    path('add_student/', views.add_student, name='add_student'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('view_student/', views.view_student, name='view_student'),
    path('view_student/<str:student_id>/', views.student_detail, name='student_detail'),
    path('delete_student/<str:student_id>/', views.delete_student, name='delete_student'),
    path('view_faculty/', views.view_faculty, name='view_faculty'),
    path('view_faculty/<str:faculty_id>/', views.faculty_detail, name='faculty_detail'),
    path('delete_faculty/<str:faculty_id>/', views.delete_faculty, name='delete_faculty'),
    path('add_admin/', views.add_admin, name='add_admin'),       # URL for adding an admin
    path('delete_admin/', views.delete_admin, name='delete_admin'), # URL for deleting an admin
    path('low_attendance_students/', views.low_attendance_students, name='low_attendance_students'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('faculty_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    # path('faculty/update-profile/<str:faculty_id>/', views.update_faculty_profile, name='update_faculty_profile'),

    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('update_profile/',views.update_profile,name='update_profile'),
   
    # path('faculty/profile/', views.faculty_profile_view, name='update_faculty_profile'),
    # path('faculty/update-profile/<int:faculty_id>/', views.update_faculty_profile, name='update_faculty_profile'),
    path('faculty_profile/', views.faculty_profile, name='faculty_profile'),
    path('update/faculty/profile/<str:faculty_id>/', views.update_faculty_profile, name='update_faculty_profile'),
    path('low-attendance/', views.low_attendance_students, name='low_attendance'),
    path('calculate_attendance/', calculate_attendance_percentage, name='calculate_attendance'),





]
