from django.shortcuts import render, redirect
from .models import User, Repos
from django.http import JsonResponse
import json

from django.views import View
from django.views import generic

# Create your views here.
class Attendance(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'attendance/index.html'
        users = User.objects.all()
        repo = Repos.objects.all()
        return render(request, template_name, {"users": users}, {"repos": repo})