# from django.urls import path
# from .views import StudentListCreateAPI, StudentRetrieveUpdateDestroyAPI    
# from .views import StudentAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router=DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = [
#     path("students/", StudentAPI.as_view(), name="students"),
#     path("students/<int:pk>/", StudentAPI.as_view(), name="student-detail"),
# ]



