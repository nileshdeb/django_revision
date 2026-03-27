from django.urls import path
from .views import StudentListCreateAPI, StudentRetrieveUpdateDestroyAPI    
# from .views import StudentAPI

# urlpatterns = [
#     path("students/", StudentAPI.as_view(), name="students"),
#     path("students/<int:pk>/", StudentAPI.as_view(), name="student-detail"),
# ]

urlpatterns = [
    path("students/", StudentListCreateAPI.as_view(), name="students"),
    path("students/<int:pk>/", StudentRetrieveUpdateDestroyAPI.as_view(), name="student-detail"),
]