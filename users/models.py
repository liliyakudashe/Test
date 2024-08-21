from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import Course
from django.conf import settings


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)

    def __str__(self):
        return f'Баланс пользователя {self.user.username}: {self.amount}'


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_subscriptions', default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_user_subscriptions', default=1)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now() + timedelta(days=30))

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)


    def __str__(self):
        return f'Подписка пользователя {self.username} на курс {self.course}'
