from django.urls import path
from .views import *
from . import views

app_name='blog'

urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blog_list,name='blogs'),
    path('author/',author,name='author'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),

]