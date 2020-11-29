from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib import auth

from .forms import AddPostForm
from . import templates


# Create your views here.


def index(request):
    post_list = BlogPost.objects.order_by('-data_post')
    return render(request, 'main_blog/index.html',
                  {'post_list': post_list, 'user_name': auth.get_user(request).username})


def user_auth(request):
    return render(request, 'main_blog/auth.html', {'user_name': auth.get_user(request).username})


def create_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = AddPostForm
    context = {'form': form}
    return render(request, 'main_blog/create_post.html', context)  # TODO fix statik data and author
