from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name": "Nilesh Deb",
        "age": 22,
        "skill": ["python", "django", "React"],
        "user": User("Kumar", 30),
        "blog": {
            "title": "Django Template Intro",
            'author':{
                "name": "Nilesh Deb",
                
            },
            "content": "<b>This is Bold</b>",
            "created_at": datetime(2026, 3, 6, 10, 30)
        },
        "empty_value": None,
    }

    return render(request, "blog/home.html", context)