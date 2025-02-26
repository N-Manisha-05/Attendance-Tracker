from django.contrib.auth.backends import BaseBackend
from .models import Admin

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            admin = Admin.objects.get(username=username)
            if admin.password == password:  # Replace with hashed password check if used
                return admin
        except Admin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            return None
