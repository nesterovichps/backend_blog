# Generated by Django 3.1.3 on 2020-11-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogger_name', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Блогер',
                'verbose_name_plural': 'Блогеры',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.CharField(max_length=50, verbose_name='Подписчики')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_blog.blogger')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_post', models.TextField(verbose_name='Текст статьи')),
                ('data_post', models.DateTimeField(verbose_name='Дата публикации')),
                ('list_post_writen', models.CharField(max_length=50, verbose_name='Прочитанные статьи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_blog.blogger')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
