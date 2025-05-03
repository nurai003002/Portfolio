from django.contrib import admin

from apps.settings import models
# Register your models here.

class ResumeInlineTabularInline(admin.TabularInline):
    model = models.ResumeInline
    extra = 1
    
class TestimonialsInlineTabularInline(admin.TabularInline):
    model = models.TestimonialsInline
    extra = 1

@admin.register(models.MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')
    
@admin.register(models.IntroductionBanner)
class IntroductionBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
@admin.register(models.MyWorks)
class MyWorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    
@admin.register(models.AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    
@admin.register(models.Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    
@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_title', 'description')
    inlines = (ResumeInlineTabularInline, )

@admin.register(models.FavouriteTools)
class FavouriteToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(models.Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_title')
    inlines = (TestimonialsInlineTabularInline,)
    
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')