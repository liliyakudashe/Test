from django.urls import include, path
from django.contrib import admin

app_name = 'api'

urlpatterns = [
    # path('v1/', include('api.v1.urls')),
    path('admin/', admin.site.urls)
]
