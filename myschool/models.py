from email.policy import default
from pyexpat import model
from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    tsc_no =models.IntegerField()
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=50, default= '')
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adm_no = models.IntegerField()
    form = models.CharField(max_length=5)
    parent_name =models.CharField(max_length=50)
    parent_phone = models.IntegerField()

    def __str__(self):
        return self.f_name

class Fee(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    paid = models.IntegerField()
    balance =models.IntegerField()


class Scores(models.Model):
    year = models.IntegerField()
    term = models.IntegerField()
    english = models.IntegerField()
    kiswahili = models.IntegerField()
    mathematics = models.IntegerField()
    physics = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()

    def __str__(self):
        return self.year

class Staff(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=50, default='')
    role = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)

    def __str__(self):
        return self.name