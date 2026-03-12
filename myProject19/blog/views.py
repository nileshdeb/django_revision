from django.shortcuts import render
from .models import Post
from django.db.models import Q

def post_list(request):
    query = request.GET.get("q") # search keyword
    category = request.GET.get("category") # category filter

    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )
 # filter by category 
    if category:
        posts = posts.filter(category__iexact=category)

    # the template file in this project is named 'blog_list.html' instead of 'post_list.html'
    # either rename the file or update the reference accordingly. we'll render the actual filename.
    return render(request, "blog/blog_list.html", {
        "posts": posts,
        "query": query,
        "category": category,
    })
