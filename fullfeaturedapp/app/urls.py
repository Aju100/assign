from .views import LoginView,SignupView,LogoutView,BlogPostView,ProfileView,ProfileUpdateView
from django.urls import path

urlpatterns = [
    path('',BlogPostView.as_view(),name='posts'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/update',ProfileUpdateView.as_view(),name='profile_update'),
]