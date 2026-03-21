from django.shortcuts import render
from .models import UserList
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.core.cache import cache

# @cache_page(30)
# def user_list(request):
#     print("Fetching data from database")
#     users = UserList.objects.all()
#     return render(request, 'users.html', {'users': users})

def user_list(request):
    users = UserList.objects.all()
    return render(request, 'users.html', {'users': users})

def clear_cache(request):
    cache.clear()
    return HttpResponse('user_list')