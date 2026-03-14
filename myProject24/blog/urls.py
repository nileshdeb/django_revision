from django.urls import path
from . import views

urlpatterns = [
    path("set-cookie/", views.set_cookie, name="set-cookies"),
    path("get-cookie/", views.get_cookie, name="get-cookies"),
    path("delete-cookie/", views.delete_cookie, name="delete-cookies"),
] 