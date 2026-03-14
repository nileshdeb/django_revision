from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(request):
    request.session['username'] = 'Nilesh'
    request.session['course'] = 'Django'
    return HttpResponse("Session set successfully")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Unknown')
    return HttpResponse(f"Welcome: {username}, You are learning: {course}")

def delete_session(request):
    request.session.flush()
    return HttpResponse("Session deleted successfully")
