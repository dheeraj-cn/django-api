import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from userapp.models import User, Project, UserProject, MentorProject, MentorMentee
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from userapp.serial import UserSerializer, ProjectSerializer, UserProjectSerial, MentorProjectSerial, MentorMenteeSerial

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserProjectViewSet(viewsets.ModelViewSet):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerial

class MentorProjectViewSet(viewsets.ModelViewSet):
    queryset = MentorProject.objects.all()
    serializer_class = MentorProjectSerial

class MentorMenteeViewSet(viewsets.ModelViewSet):
    queryset = MentorMentee.objects.all()
    serializer_class = MentorMenteeSerial

# class MenteesViewSet(viewsets.ModelViewSet):
#     queryset = MentorMentee.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             return Response("Wrong method", status=400)
#         elif request.method == 'POST':
#             data = json.loads(request.body)
#             mentor_id = data["mentor"]
#             dt = MentorProject.objects.values_list('project').filter(mentor=mentor_id)
#             res = []
#             dictAnswer = {}
#             for i in dt:
#                 res += (i)
#             dictAnswer["Projects"] = res
#             return Response(dictAnswer, safe=False)

@csrf_exempt
def UserHandler(request):
    if request.method=='GET':
        all_users = User.objects.all()
        user_list = UserSerializer(all_users,many=True)
        return JsonResponse(user_list.data,safe=False)
    else:
        print(request.body)
        data = json.loads(request.body)
        user = UserSerializer(data=data)
        if user.is_valid():
            user.save()
            return HttpResponse("Done",status=201)
        else:
            return HttpResponse("ERROR",status=400)

@csrf_exempt
def ProjectHandler(request):
    if request.method=='GET':
        all_projects = Project.objects.all()
        project_list = ProjectSerializer(all_projects,many=True)
        return JsonResponse(project_list.data,safe=False)
    else:
        #print(request.body)
        data = json.loads(request.body)
        project = ProjectSerializer(data=data)
        if project.is_valid():
            project.save()
            return HttpResponse("Done",status=201)
        else:
            return HttpResponse("ERROR",status=400)

@csrf_exempt
def UserProjectHandler(request):
    if request.method == 'GET':
        all_relation = UserProject.objects.all()
        lst = UserProjectSerial(all_relation,many=True)
        return JsonResponse(lst.data,safe=False)

    else:
         print(request.body)
         data = json.loads(request.body)
         print(data)
         project_id = data["project"]
         for u in data['users']:
             dt = UserProject(project=Project.objects.get(pk=project_id),user=User.objects.get(pk=u))
             dt.save()

         return HttpResponse("OK",status=200)

@csrf_exempt
def MentorProjectHandler(request):
    if request.method =='GET':
        all_relation = MentorProject.objects.all()
        lst = MentorProjectSerial(all_relation, many=True)
        return JsonResponse(lst.data, safe=False)
    else:
        data = json.loads(request.body)
        mentorProject = MentorProjectSerial(data = data)
        if mentorProject.is_valid():
            mentorProject.save()
            return HttpResponse("Done",status=201)
        else:
            return HttpResponse("ERROR",status=400)


@csrf_exempt
def MentorMenteeHandler(request):
    if request.method == 'GET':
        all_relation = MentorMentee.objects.all()
        lst = MentorMenteeSerial(all_relation,many=True)
        return JsonResponse(lst.data,safe=False)
    else:
         data = json.loads(request.body)
         mentor_id = data["mentor"]
         for u in data['mentee']:
             if u == mentor_id:
                 continue
             dt = MentorMentee(mentor=User.objects.get(pk=mentor_id),mentee=User.objects.get(pk=u))
             dt.save()

         return HttpResponse("OK",status=200)

@csrf_exempt
def get_mentees(request):
    if request.method=='GET':
        return HttpResponse("Wrong menthod",status=400)
    elif request.method == 'POST':
        data = json.loads(request.body)
        mentor_id = data["mentor"]
        dt = MentorMentee.objects.values_list('mentee').filter(mentor = mentor_id)
        res = []
        dictAnswer = {}
        for i in dt:
            res.append(i)
        dictAnswer["Mentees"] = res
        return JsonResponse(dictAnswer,safe=False)

@csrf_exempt
def get_mentor_projects(request):
    if request.method=='GET':
        return HttpResponse("Wrong menthod",status=400)
    elif request.method == 'POST':
        data = json.loads(request.body)
        mentor_id = data["mentor"]
        dt = MentorProject.objects.values_list('project').filter(mentor=mentor_id)
        res = []
        dictAnswer = {}
        for i in dt:
            res+= (i)
        dictAnswer["Projects"] = res
        return JsonResponse(dictAnswer,safe=False)

@csrf_exempt
def get_user_and_mentors_of_project(request):
    if request.method == 'GET':
        return HttpResponse("Wrong method",status=400)
    elif request.method == 'POST':
        data = json.loads(request.body)
        project_id = data["project"]
        dt = MentorProject.objects.values_list('mentor').filter(project=project_id)
        dt2 = UserProject.objects.values_list('user').filter(project=project_id)
        res = []
        res2 = []
        dictAnswer= {}
        for i in dt:
            res+=(i)
        for i in dt2:
            res2+=(i)
        dictAnswer["mentors"] = res
        dictAnswer["users"] = res2
        return JsonResponse(dictAnswer,safe=False)