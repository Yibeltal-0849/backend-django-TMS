from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Root path - THIS IS WHAT'S MISSING
    path('', lambda request: HttpResponse("Welcome to Task Manager API")),
    
    path('admin/', admin.site.urls),

    # JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Don't forget to include your projects and tasks URLs too!
    path('api/', include('apps.projects.urls')),
    path('api/', include('apps.tasks.urls')),
]