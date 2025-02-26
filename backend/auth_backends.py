from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentIDAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Replace 'username' with 'student_id'
        student_id = kwargs.get('student_id', username)
        try:
            user = User.objects.get(student_id=student_id)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
