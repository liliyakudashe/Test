from django.urls import include, path
from django.contrib import admin

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
]
