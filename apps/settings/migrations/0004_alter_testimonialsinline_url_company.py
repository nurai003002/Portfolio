# Generated by Django 5.0.6 on 2025-05-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_introductionbanner_cv_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialsinline',
            name='url_company',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ссылка на сайт'),
        ),
    ]
