from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"<h1>BlogPost details page. Post id: {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Blog, user profile page. Username: {username}</h1>")

def artical_by_year(request, year):
    return HttpResponse(f"<h1>Blog, artical by year page. Year: {year}</h1>")    

def article_details(request, year, month, ):
    return HttpResponse(f"<h1>Articles from {year} - {month}</h1>")   