# from django.urls import include, path
# from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
#                                    SpectacularSwaggerView)
# from rest_framework.routers import DefaultRouter
#
# from api.v1.views.course_view import CourseViewSet, GroupViewSet, LessonViewSet
# from api.v1.views.user_view import UserViewSet
#
# v1_router = DefaultRouter()
# v1_router.register('users', UserViewSet, basename='users')
# v1_router.register('courses', CourseViewSet, basename='courses')
# v1_router.register(
#     r'courses/(?P<course_id>\d+)/lessons', LessonViewSet, basename='lessons'
# )
# v1_router.register(
#     r'courses/(?P<course_id>\d+)/groups', GroupViewSet, basename='groups'
# )
#
# urlpatterns = [
#     path("", include(v1_router.urls)),
#     path("auth/", include('djoser.urls')),
#     path("auth/", include('djoser.urls.authtoken')),
#     # Создание нового пользователя api/v1/auth/users/
#     # Авторизация пользователя     api/v1/auth/token/login/
# ]
#
# urlpatterns += [
#     path(
#         'schema/',
#         SpectacularAPIView.as_view(api_version='api/v1'),
#         name='schema'
#     ),
#     path(
#         'swagger/',
#         SpectacularSwaggerView.as_view(url_name='schema'),
#         name='swagger-ui',
#     ),
#     path(
#         'redoc/',
#         SpectacularRedocView.as_view(url_name='schema'),
#         name='redoc',
#     ),
# ]

from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from .views.course_view import course_list

from api.v1.views.course_view import CourseViewSet, GroupViewSet, LessonViewSet
from api.v1.views.user_view import UserViewSet

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='user')
v1_router.register('courses', CourseViewSet, basename='course')
v1_router.register(r'courses/(?P<course_id>\d+)/lessons', LessonViewSet, basename='course-lessons')
v1_router.register(r'courses/(?P<course_id>\d+)/groups', GroupViewSet, basename='course-groups')

urlpatterns = [
    path('api/v1/', include('api.v1.urls')),  # Ensure proper nesting
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/views/course_view/', course_list, name='course_list')
]

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]