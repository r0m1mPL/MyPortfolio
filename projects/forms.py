from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message',)
