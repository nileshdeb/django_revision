from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    blogs=[
        {"title":"Django Basics","is_featured":True,"auther":"Nilesh Deb"},
        {"title":"Django Models","is_featured":False,"auther":""},
        {"title":"Django Views","is_featured":True,"auther":"jane"},
    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>This is bold text</h1>"

    }
    return render(request, "blog/blog_list.html",context)   
# Create your views here.
