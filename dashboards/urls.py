from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("categories/", views.categories, name='categories'),
    path("categories/add", views.add_category, name='add_category'),
    path("categories/edit/<slug:category_slug>/", views.edit_category, name='edit_category'),
    path("categories/delete/<slug:category_slug>/", views.delete_category, name='delete_category'),
]
