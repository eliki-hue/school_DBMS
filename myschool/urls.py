from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('' , views.dashboard , name='dashboard'),
    path('teachers', views.teachers, name ='teachers'),
    path('students', views.students, name='students'),
    path('staff', views.staff, name='staff' ),
    path('add_student', views.add_student, name='add_student'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('search/', views.search_results, name='search_results'),
    path("neighbourhood/<str:pk>/", views.single_neighbourhood, name='single_neighbourhood'),
    
]