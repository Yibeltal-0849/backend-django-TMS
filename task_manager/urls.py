# from django.http import HttpResponse
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/projects/', include('apps.projects.urls')),
#     path('api/tasks/', include('apps.tasks.urls')),

#     # Root path
#     path('', lambda request: HttpResponse("Welcome to Task Manager API")),
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('apps.projects.urls')),
    path('api/', include('apps.tasks.urls')),
]
