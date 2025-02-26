from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Default Django admin
    path('', include('backend.urls')),  # Include backend URLs (custom admin login and others)
]
