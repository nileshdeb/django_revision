from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
    response = HttpResponse("Cookie set successfully")
    response.set_cookie("username", "Nilesh",max_age=60*60*24)# 1 day
    response.set_cookie("course", "Django full course",max_age=60*60*24) # 1 day
    return response

def get_cookie(request):
    username = request.COOKIES.get("username",'Guest')
    course = request.COOKIES.get("course",'no course selected')
    if "username" in request.COOKIES:
        return HttpResponse(f"Welcome: {username}, You are learning: {course}")
    else:
        return HttpResponse("No cookie found")

def delete_cookie(request):
    response = HttpResponse("Cookie deleted successfully")
    response.delete_cookie("username")
    response.delete_cookie("course")
    return response