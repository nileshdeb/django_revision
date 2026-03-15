from django.shortcuts import render
from django.http import HttpResponse
from .models import YouTubeUser
from django.core.cache import cache

def users_list(request):
    users=cache.get('users_data')

    if not users:
        print("cache miss: Fetching data from database") 
        users = YouTubeUser.objects.all()
        cache.set('users_data',users,timeout=300)

    else :
        print('cache hit: Fetching data from cache')    
        
    return render(request,'user_list.html',{'users':users})    