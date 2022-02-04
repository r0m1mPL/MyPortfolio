from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin-panel/', admin.site.urls),

    path('', views.index, name='home'),

    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
