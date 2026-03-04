from django.urls import path,re_path
from . import views

urlpatterns = [
    path("post/<int:post_id>/", views.post_details, name="post-details"),
    path("user/<str:username>/", views.user_profile, name="user-profile"),
    path("article/<int:year>/<int:month>/", views.article_details, name="article-details"),
    re_path(r"article/(?P<year>\d{4})/$", views.artical_by_year, name="articles-by-year"),
]