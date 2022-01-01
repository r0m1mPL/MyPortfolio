from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Project(models.Model):
    """Проект"""
    title = models.CharField("Заголовок", max_length=100)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    main_image = models.ImageField(
        "Изображение", upload_to='projects/', default="projects/standart_project_icon.png")
    short_description = models.CharField("Краткое описание", max_length=150)
    description = models.TextField("Описание")
    github_video_url = models.URLField(
        "Ссылка на проект или видео", max_length=160, default='')
    pub_date = models.DateTimeField("Дата публикации", default=timezone.now)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.url})


class ProjectImages(models.Model):
    """Картинки к проекту"""
    image = models.ImageField("Изображение", upload_to="projects/")
    project = models.ForeignKey(
        Project, verbose_name="Проект", on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Картинка к проекту"
        verbose_name_plural = "Картинки к проекту"


class Message(models.Model):
    """Messages"""
    name = models.CharField("Full name", max_length=100)
    email = models.EmailField("Email")
    subject = models.CharField("Subject", max_length=200)
    message = models.TextField("Message")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
