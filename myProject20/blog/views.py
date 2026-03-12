from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html" # specify the template name
    context_object_name = "posts" # specify the context variable name


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html" # specify the template name
    context_object_name = "post" # specify the context variable name

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html" # specify the template name
    fields = ["title", "content"] # specify the fields to include in the form   

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html" # reuse the same template for create and update
    fields = ["title", "content"] # specify the fields to include in the form

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html" # specify the template name
    success_url = reverse_lazy("post_list") # redirect to post list after deletion            