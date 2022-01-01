from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/categories/', views.category_list, name='category_list'),
    path('projects/categories/<str:slug>/',
         views.category_detail, name='category_detail'),
    path('projects/<str:slug>/<str:pk>/',
         views.project_detail, name='project_detail'),
    path('message_list/', views.message_list, name="message_list"),
]
