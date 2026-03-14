from django.urls import path
from . import views

urlpatterns = [
    path('set-session/', views.set_session, name='set-session'),
    path('get-session/', views.get_session, name='get-session'),
    path('delete-session/', views.delete_session, name='delete-session'),
]