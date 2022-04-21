from email.policy import default
from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    adm_no = models.IntegerField()
    tsc_no =models.IntegerField()
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
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