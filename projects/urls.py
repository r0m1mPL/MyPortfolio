from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.error, name='error'),

    path('', views.index, name='home'),

    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
