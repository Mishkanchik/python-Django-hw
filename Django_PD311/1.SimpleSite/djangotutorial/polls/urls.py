from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', views.users, name='users'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='create_post'),
]
