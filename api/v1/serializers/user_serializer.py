from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers
from users.models import CustomUser



from api.v1.serializers.course_serializer import StudentSerializer, CourseSerializer
from courses.models import Subscription

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    user = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
            'start_date',
        )
