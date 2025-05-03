from django.db import models

# Create your models here.
class   MyInformation(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    avatar = models.ImageField(
        upload_to='avatar/',
        verbose_name='Аватар'
    )
    specialization = models.CharField(
        max_length=200,
        verbose_name='Спецализация'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Местоположение'
    )
    instagram = models.URLField(
        verbose_name='URL instagram',
        blank=True, null=True
    )
    linkedin = models.URLField(
        verbose_name='URL linkedin',
        blank=True, null=True
    )
    telegram = models.URLField(
        verbose_name='URL telegram',
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name='URL whatsapp',
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=23,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Информация обо мне'
        verbose_name_plural = 'Информаиця обо мне'
    
class IntroductionBanner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    cv_resume = models.FileField(
        verbose_name='URL резюме',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Текст (баннер)'
        verbose_name_plural = 'Текст (баннер)'
        
        
class MyWorks(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название работы'
    )
    image = models.ImageField(
        upload_to='works/',
        verbose_name='Фото сайта'
    )
    tags = models.CharField(
        max_length=255,
        verbose_name='Теги'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание работы'
    )
    link = models.URLField(
        verbose_name='URL работы',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    
    def __str__(self):
        return f"{self.title} - {self.description}"
    
    class Meta:
        verbose_name = 'Мои проекты'
        verbose_name_plural = 'Мои проекты'
        
class AboutMe(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    clients = models.PositiveIntegerField(
        verbose_name='Кол-во клиентов'
    )
    experience = models.PositiveIntegerField(
        verbose_name='Опыт работы'
    )
    projects_amount = models.PositiveIntegerField(
        verbose_name='Кол-во проектов'
    )
      
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Об о мне'
        verbose_name_plural = 'Об о мне'
      
class Skills(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    tool_1 = models.CharField(
        max_length=100,
        verbose_name='Инструмент 1'
    )
    tool_2 = models.CharField(
        max_length=100,
        verbose_name='Инструмент 2'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Короткое описание'
    )
    image = models.ImageField(
        upload_to='about_me/',
        verbose_name='Фото'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Скил'
        verbose_name_plural = 'Скилы'
        
class Resume(models.Model):
    main_title = models.CharField(
        max_length=100,
        verbose_name='Главный заголовок'
    )
    description = models.CharField(
        max_length=300,
        verbose_name='Главное описание'
    )
    
    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        
class ResumeInline(models.Model):
    CHOICE = [
        ('My education', 'My education'),
        ('Work experience', 'Work experience'),
    ]
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE,
        related_name='resume_inline'
    )
    chioce = models.CharField(
        max_length=255,
        choices=CHOICE,
        verbose_name='Выбор'
    )
    year = models.CharField(
        max_length=100,
        verbose_name='Даты',
        default='2015-2016'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='На кого училась'
    )
    title_of_school = models.CharField(
        max_length=100,
        verbose_name='Название училища'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Краткое описание'
    )
    
    def __str__(self):
        return f"{self.position} - {self.year}"
    
    class Meta:
        verbose_name = 'Доп. информация'
        verbose_name_plural = 'Доп. информация'
    
class FavouriteTools(models.Model):
    icon = models.ImageField(
        upload_to='tools/',
        verbose_name='Иконка'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
        
class Testimonials(models.Model):
    main_title = models.CharField(
        max_length=255,
        verbose_name='Главный заголовок'
    )
    
    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
class TestimonialsInline(models.Model):
    tesimonials = models.ForeignKey(
        Testimonials, on_delete=models.CASCADE,
        related_name='tesimonials'
    )
    image = models.ImageField(
        upload_to='tesimonial/',
        verbose_name='Фото user'
    )
    fullname = models.CharField(
        max_length=255,
        verbose_name='Полное имя'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Позиция'
    )
    company = models.CharField(
        max_length=255,
        verbose_name='Название компании'
    )
    url_company = models.URLField(
        verbose_name='Ссылка на сайт',
        blank=True, null=True
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.fullname} - {self.comment}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    company = models.CharField(
        max_length=255,
        verbose_name='название компании'
    )
    email = models.EmailField(
        verbose_name='Почта',
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=23,
        verbose_name='Номер телефона'
    )
    message = models.CharField(
        max_length=500,
        verbose_name='доп. информация'
    )
    
    def __str__(self):
        return f"{self.name} - {self.message}"
    
    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'