from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth, name='auth'),
    path('create_post', views.create_post, name='create_post'),

]