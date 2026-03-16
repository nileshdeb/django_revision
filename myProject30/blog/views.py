from django.shortcuts import render
from .models import UserList
from django.views.decorators.cache import cache_page

@cache_page(30)
def user_list(request):
    print("Fetching data from database")
    users = UserList.objects.all()
    return render(request, 'users.html', {'users': users})