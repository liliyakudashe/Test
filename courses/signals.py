from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Subscription


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """
    if created:
        course = instance.course
        groups = course.groups.order_by('student_count')
        for group in groups:
            if group.student_count < group.max_students:
                group.student_count += 1
                group.save()
                break
