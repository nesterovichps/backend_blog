from django.shortcuts import render
from .models import Blog_post
from . import templates
# Create your views here.


def index(request):
    post_list=Blog_post.objects.all()
    return render(request, 'main_blog/index.html', {'post_list': post_list})


def auth(request):
    return render(request, 'main_blog/auth.html')

def create_post(request):

    return render(request, 'main_blog/create_post.html') #TODO fix statik data and author