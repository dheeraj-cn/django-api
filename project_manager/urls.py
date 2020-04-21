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
from rest_framework_swagger.views import get_swagger_view

from userapp.models import User
from userapp.serial import UserSerializer
from userapp.views import UserHandler, ProjectHandler, UserProjectHandler, MentorProjectHandler, MentorMenteeHandler, \
    get_mentees, get_mentor_projects, get_user_and_mentors_of_project, UserViewSet, ProjectViewSet, UserProjectViewSet, \
    MentorProjectViewSet, MentorMenteeViewSet, MenteesView
from rest_framework.documentation import include_docs_urls

#schema_view = get_swagger_view(title='Swagger Docs')



router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'userprojects',UserProjectViewSet)
router.register(r'mentorprojects',MentorProjectViewSet)
router.register(r'mentormentees',MentorMenteeViewSet)
# router.register(r'mentees',MenteesView)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('users',UserHandler),
    #path('project',ProjectHandler),
    #path('userproject',UserProjectHandler),
    #path('mentorproject',MentorProjectHandler),
    #path('mentormentee',MentorMenteeHandler),
    # path('mentees',MenteesView.as_view()),
    # path('mentoring',get_mentor_projects),
    # path('projectmembers',get_user_and_mentors_of_project),
]
