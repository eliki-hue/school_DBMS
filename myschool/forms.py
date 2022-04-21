from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher, Scores, Student, Fee

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
       
        fields ='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        
        fields ='__all__'

class ScoresForm(forms.ModelForm):
    class Meta:
        model= Scores
        fields='__all__'


class FeeForm(forms.ModelForm):
   
    class Meta:
        model= Fee
        fields='__all__'