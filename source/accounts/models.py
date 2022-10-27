from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager

class Sex(models.Model):
    title = models.CharField(
        verbose_name='Пол',
        max_length=10,
        null=False,
        blank=False
    )
    title_rus = models.CharField(
        verbose_name='Пол (рус)',
        max_length=10,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return self.title_rus


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    information = models.CharField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Информация о пользователе'
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        null=True,
        blank=True,
        max_length=20
    )
    sex = models.ForeignKey(
        to='accounts.Sex',
        on_delete=models.CASCADE,
        related_name='sex_accounts',
        verbose_name='Пол',
        blank=True,
        null=True
    )
    # liked_posts = models.ManyToManyField(verbose_name='Понравившиеся публикации', to='posts.Post', related_name='user_likes', null=True, blank=True)
    # subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Account', related_name='subscribers', null=True, blank=True)
    # commented_posts = models.ManyToManyField('Прокомментированные публикации', to='posts.Post', related_name='user_comments')

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
