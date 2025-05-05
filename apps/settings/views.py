from django.shortcuts import render, redirect

from apps.settings import models
from apps.telegram_bot.views import get_text
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
    
    success = False
    if request.method == 'POST':
        if 'contact_form' in request.POST:
            name = request.POST.get('name')
            company = request.POST.get('company')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            page_contact = models.Contact.objects.create(
                name=name,
                company=company,
                email=email,
                phone=phone,
                message=message,)
            if page_contact:
                get_text(f"""
                     Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Компания:  {company}
Почта: {email}
Номер телефона: {phone}
Сообщение: {message}
                     """)
            return redirect('index')
    return render(request, 'base/index.html', locals())