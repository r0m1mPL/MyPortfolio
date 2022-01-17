from django.contrib.auth import models
from django.forms import ModelForm, fields
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
