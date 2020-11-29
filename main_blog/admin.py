from django.contrib import admin
from .models import BlogPost, Blogger, Subscribe

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Blogger)
admin.site.register(Subscribe)
