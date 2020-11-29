from django.db import models


# Create your models here.
class Blogger(models.Model):
    blogger_name = models.CharField('Автор', max_length=50)  # TODO fixto dinamik

    def __str__(self):
        return (self.blogger_name)

    class Meta:
        verbose_name = 'Блогер'
        verbose_name_plural = 'Блогеры'


class BlogPost(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    text_post = models.TextField('Текст статьи')  # TODO views only subskribe post
    data_post = models.DateTimeField('Дата публикации')  # TODO add auto date
    list_post_writen = models.CharField('Прочитанные статьи', max_length=50)  # TODO check on correct work

    def __str__(self):
        return (self.text_post)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Subscribe(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    subscribe = models.CharField('Подписчики', max_length=50)

    def __str__(self):
        return (self.subscribe)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
