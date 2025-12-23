from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('apps.projects.urls')),
    path('api/tasks/', include('apps.tasks.urls')),

    # Root path
    path('', lambda request: HttpResponse("Welcome to Task Manager API")),
]
