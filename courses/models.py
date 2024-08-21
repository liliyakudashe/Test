from django.db import models
from django.conf import settings



class Course(models.Model):
    """Модель продукта - курса."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
        )
    author = models.CharField(
        max_length=250,
        verbose_name='Автор',
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        default=0.00
    )

    max_students = models.PositiveIntegerField(
        default=30,
        verbose_name='Максимальное количество студентов',
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель урока."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )

    course = models.ForeignKey(
        Course,
        related_name='lessons',
        on_delete=models.CASCADE,
        verbose_name='Курс',
        default=1
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель группы."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
        default='Default'
    )

    course = models.ForeignKey(
        Course,
        related_name='groups',
        on_delete=models.CASCADE,
        verbose_name='Курс',
        default=1
    )

    max_students = models.PositiveIntegerField(
        default=30,
        verbose_name='Максимальное количество студентов',
    )

    student_counts = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество студентов',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Мщдель подписки пользователя на курс"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='course_subscriptions'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        related_name='user_course_subscriptions',
        default=1,
    )

    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата начала подписки',
    )

    class Meta:
        verbose_name = 'Подписка',
        verbose_name_plural = 'Подписки',
        ordering = ('-id',)
