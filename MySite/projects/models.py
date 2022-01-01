from django.db import models


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
