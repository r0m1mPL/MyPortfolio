from django.urls import path
from . import views
from MySite.views import admin


urlpatterns = [
    path('admin/', admin, name='admin'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
