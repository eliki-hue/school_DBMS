from django.contrib import admin
from .models import Teacher, Scores, Student, Fee

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Scores)
admin.site.register(Student)
admin.site.register(Fee)
