from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('blogs/<slug:url>', views.post, name='post'),
    path('category/<slug:url>', views.category, name='category'),
    path('logout/' , LogoutView.as_view(next_page = 'blogs:home'), name='logout'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('about/', views.about, name='about'),
]