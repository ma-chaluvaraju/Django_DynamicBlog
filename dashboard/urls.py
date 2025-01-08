from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # categories
    path('categories/', views.categories, name='categories'),
    path('categories/add', views.add_categories, name='add_categories'),
    path('categories/edit/<int:pk>', views.edit_categories, name='edit_categories'),
    path('categories/delete/<int:pk>', views.delete_categories, name='delete_categories'),

    # posts
    path('posts/', views.posts, name="posts"),
    path('posts/add/', views.add_posts, name="add_posts"),
    path('posts/edit/<int:pk>/', views.edit_posts, name="edit_posts"),
    path('posts/delete/<int:pk>/', views.delete_posts, name="delete_posts"),

    # user
    path('users/', views.users, name="users"),
    # path('users/add/', views.add_users, name="add_users"),
    path('users/edit/<int:pk>/', views.edit_user, name="edit_user"),
    path('users/delete/<int:pk>/', views.delete_user, name="delete_user")

]