from django.contrib import admin

from apps.secondary.models import Team, Reviews, News, Partner, Progres, Pricing, PricingService, TeamInfo, TeamInfoDop
# Register your models here.

class PricingSeviceTaburaInline(admin.TabularInline):
    model = PricingService
    extra = 1
    
class TeamInfoTaburaInline(admin.TabularInline):
    model = TeamInfo
    extra = 1
    
class TeamInfoDopTaburaInline(admin.TabularInline):
    model = TeamInfoDop
    extra = 1
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    inlines = [TeamInfoTaburaInline, TeamInfoDopTaburaInline]
    
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image', )
    
@admin.register(Progres)    
class ProgresAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    
