from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post={
        'title':"My second Templates Post",
        "description":"Django Template is very useful for rendering dynamic data in HTML. It provides a powerful and flexible way to create dynamic web pages by allowing you to embed Python code within your HTML templates. With Django Template, you can easily display data from your database, perform logic operations, and create reusable components for your web application.",
        "author":None,
        "created_at":datetime(2026,3,6,10,30),
        'comments_count':5,
        'tags':["django","python","web development"],
        'price':100,
        'number':2
    }
    return render(request, "blog/blog_details.html", {"post": post})
# Create your views here.
