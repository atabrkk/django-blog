from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search, name='search'),
    path("category/<slug:category_slug>/", views.posts_by_category, name='posts_by_category'),
    path("<slug:slug>/", views.blog, name='blog'),

]
