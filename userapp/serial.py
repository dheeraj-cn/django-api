from rest_framework import serializers

from userapp.models import User, Project, UserProject, MentorProject, MentorMentee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class UserProjectSerial(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = '__all__'

class MentorProjectSerial(serializers.ModelSerializer):
    class Meta:
        model = MentorProject
        fields = '__all__'

class MentorMenteeSerial(serializers.ModelSerializer):
    class Meta:
        model = MentorMentee
        fields = '__all__'