# Generated by Django 4.0.3 on 2022-04-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0005_staff_email_staff_phone_teacher_email_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]