from django.shortcuts import render
from django.http import HttpResponse
from project import models
# Create your views here.


def index(request):
    data=models.Project_data.objects.all()
    return render(request,'project/index.html',{'data':data})

def show_project(request,project_id):
    data=models.Project_data.objects.filter(id=project_id)
    dist={}
    for d in data:
        dist['id']=d.id
        dist['name']=d.Name
        dist['short_desc']=d.Short_desc
        dist['intro']=d.Intro
        dist['technology']=d.Technology
        dist['module']=d.Module
        dist['git']=d.Github_link
        dist['image']=d.image
    return render(request,'project/project_desc.html',{'data':dist})
