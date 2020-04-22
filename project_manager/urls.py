"""project_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import viewsets, routers
from userapp.views import UserViewSet, ProjectViewSet, UserProjectViewSet, \
    MentorProjectViewSet, MentorMenteeViewSet

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'userprojects',UserProjectViewSet)
router.register(r'mentorprojects',MentorProjectViewSet)
router.register(r'mentormentees',MentorMenteeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Django Test REST API",
        description="API for all things …",
        version="1.0.0",
        url="http://127.0.0.1:8000"
    ), name='openapi-schema'),
]
