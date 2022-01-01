from django.contrib import admin
from projects.models import Category, Project, ProjectImages, Message


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('name', 'url',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Проекты"""
    list_display = ('title', 'category', 'short_description', 'main_image', 'pub_date', 'url',)


@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    """Картинки к проекту"""
    list_display = ('project', 'image',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ('name', 'email', 'subject',)
