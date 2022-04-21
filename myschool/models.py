from email.policy import default
from django.db import models
from django.forms import CharField, IntegerField
from sqlalchemy import ForeignKey

# Create your models here.
class Teacher(models.Model):
    name = CharField(max_length=50)
    adm_no = IntegerField()
    tsc_no =IntegerField()
    subject1 = CharField(max_length=20)
    subject2 = CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    f_name = CharField(max_length=30)
    l_name = CharField(max_length=30)
    form = CharField(max_length=5)
    parent_name =CharField(max_length=50)
    parent_phone = IntegerField()

    def __str__(self):
        return self.f_name

class Fee(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    paid = IntegerField()
    balance =IntegerField()


class Scores(models.Model):
    year = IntegerField()
    term = IntegerField()
    english = IntegerField()
    kiswahili = IntegerField()
    mathematics = IntegerField()
    physics = IntegerField()
    biology = IntegerField()
    chemistry = IntegerField()

    def __str__(self):
        return self.year