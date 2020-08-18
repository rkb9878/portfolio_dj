from django.db import models

# Create your models here.


class Project_data(models.Model):
    Name=models.CharField(max_length=200)
    Short_desc=models.TextField()
    Intro=models.TextField()
    Technology=models.CharField(max_length=300,blank=True,default='None')
    Module=models.CharField(max_length=300,blank=True,default='None')
    Github_link=models.CharField(max_length=300,blank=True,default='None')
    image=models.FileField(upload_to='project_image/')

    def __str__(self):
        return self.Name
