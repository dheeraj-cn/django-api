from django.contrib import admin

# Register your models here.
from userapp.models import Project, User

admin.site.register(Project)
admin.site.register(User)
