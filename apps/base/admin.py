from django.contrib import admin

from apps.base.models import Setting, Slider, About, AboutService, AboutState, AboutSkill, Choose, Contact, WorkProcessStep
# Register your models here.

class AboutServiceTabularInlain(admin.TabularInline):
    model = AboutService 
    extra = 1
    
class AboutStateTabularInlain(admin.TabularInline):
    model = AboutState 
    extra = 1

class AboutSkillTabularInlain(admin.TabularInline):
    model = AboutSkill 
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'address', 'phone', 'email')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'desc')
    
@admin.register(About)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [AboutServiceTabularInlain, AboutStateTabularInlain, AboutSkillTabularInlain]
    
@admin.register(Choose)
class ChooseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text')
    
@admin.register(WorkProcessStep)
class WorkProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title')