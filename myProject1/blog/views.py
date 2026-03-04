from django.http import HttpResponse
def home(request):
    return HttpResponse("BLOG, Home page")

def about(request):
    return HttpResponse("Blog, about page.")
# Create your views here.
