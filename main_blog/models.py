from django.db import models

# Create your models here.
class Blog_post(models.Model):

    author=models.CharField('Автор', max_length=50) #TODO fix
    text_post=models.TextField('Текст статьи') #TODO fix
    data_post=models.DateTimeField('Дата', max_length=10) #TODO fix
    # status_write=models.BooleanField('Прочитана\не прочитана', max_length=50) #TODO fix

    def __str__(self):
        return (self.text_post)
    class Meta:
        verbose_name='Пост'
        verbose_name_plural = 'Посты'
# class Subscribe(models.Model);
#     pass