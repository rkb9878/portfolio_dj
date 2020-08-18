from django.urls import path
from project.views import  index,show_project

app_name='theProject'

urlpatterns=[
    path('', index,name='index'),
    path('show_project/<int:project_id>/', show_project,name='show_project'),
]
