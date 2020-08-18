from django.contrib import admin
from project.models import Project_data
# Register your models here.

class Project_data_admin(admin.ModelAdmin):
    list_display = ('Name','Short_desc','Technology','Module','image')

    list_filter = ['Name','Short_desc','Module']

admin.site.register(Project_data,Project_data_admin)
