from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [
    path('api/v1', include('api.v1.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='courses/index.html'), name='home')
]
