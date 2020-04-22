from django.db import models


# Create your models here.
from django.utils.timezone import now


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.project_name


class MentorMentee(models.Model):
    mentor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='mentorRelation')
    mentee = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='menteeRelation')


class MentorProject(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    mentor = models.ForeignKey(to=User, on_delete=models.CASCADE)


class UserProject(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
