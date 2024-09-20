from django.contrib import admin

from apps.project.models import Project, Service, ProjectImage, ProjectInfo
# Register your models here.

class ProjectImageTaburalInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectInfoTabularInline(admin.TabularInline):
    model = ProjectInfo
    extra = 1 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [ProjectImageTaburalInline, ProjectInfoTabularInline]
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
        