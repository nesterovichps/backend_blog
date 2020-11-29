from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('user_auth', views.user_auth, name='user_auth'),
    path('create_post', views.create_post, name='create_post'),
    path('accounts/', include('django.contrib.auth.urls'), name='user_auth'),
]
