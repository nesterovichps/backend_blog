from .models import BlogPost
from django.forms import ModelForm, Textarea


class AddPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['author', 'text_post', 'data_post']
        widgets = {'text_post': Textarea(attrs={
            "name": "new_post",
            "cols": "150",
            "rows": "10",
            "placeholder": "Введите текст"
        }), }
