from django.shortcuts import render
from .models import Author, Post
from django.views import generic

def home(request):
    return render(request,'blog/home.html')

def blog_list(request):
    blogs = Post.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blog/blogs.html',context=context)

def author(request):
    author_name = Author.objects.all()

    context = {
        'author_name':author_name
    }
    return render(request,'blog/author_list.html',context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'