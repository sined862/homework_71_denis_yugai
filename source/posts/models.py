from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    description = models.CharField(
        max_length=300,
        verbose_name='Описание публикации',
        null=False,
        blank=False
    )
    image = models.ImageField(
        verbose_name='Фото публикации',
        null=False,
        blank=False,
        upload_to='posts'
    )
    author = models.ForeignKey(
        verbose_name='Автор публикации',
        to=get_user_model(),
        related_name='posts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='comments',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Публикация',
        to='posts.Post',
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=200,
        verbose_name='Текст',
        null=False,
        blank=False,
        default=''
    )
    