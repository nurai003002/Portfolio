from django.shortcuts import render

from apps.settings import models

# Create your views here.

def index(request):
    my_information = models.MyInformation.objects.latest('id')
    intro_banner = models.IntroductionBanner.objects.latest('id')
    my_works = models.MyWorks.objects.all()
    about_me = models.AboutMe.objects.latest('id')
    skills = models.Skills.objects.all()
    resume = models.Resume.objects.latest('id')
    favourite_tools = models.FavouriteTools.objects.all()
    testimonials = models.Testimonials.objects.latest('id')
    return render(request, 'base/index.html', locals())