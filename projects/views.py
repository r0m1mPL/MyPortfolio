from django.shortcuts import render, redirect
from projects.models import Message
from .forms import MessageForm
from django.contrib import messages
from django.http import Http404
from datetime import datetime


def error(request):
    raise Http404("You're not allowed here!")


def index(request):
    date = list(map(int, datetime.now().strftime("%Y %m %d").split()))
    age = date[0] - 2005 if date[1] >= 4 and date[2] >= 16 else date[0] - 2006

    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            if len(request.POST.get('name').split()) in [2, 3]:
                if request.POST.get('email').lower():
                    email = request.POST.get('email')
                    if Message.objects.filter(email=email).count() >= 3:
                        messages.error(
                            request, "You can't send more than 3 messages!")
                        return redirect('/#contact')
                    form.save()
                    messages.error(request, "Message has been sent!")
                    return redirect('/#contact')
                else:
                    messages.error(
                        request, "Email is incorrect or doesn't exist!")
                    return redirect('/#contact')
            else:
                messages.error(request, "Full name is incorrect!")
                return redirect('/#contact')

    return render(request, 'projects/index.html', {'form': form, 'age': age})


def about(request):
    date = list(map(int, datetime.now().strftime("%Y %m %d").split()))
    age = date[0] - 2005 if date[1] >= 4 and date[2] >= 16 else date[0] - 2006
    return render(request, 'projects/include/about.html', {'check_main': True, 'age': age})


def resume(request):
    return render(request, 'projects/include/resume.html', {'check_main': True})


def contact(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            if len(request.POST.get('name').split()) in [2, 3]:
                if request.POST.get('email').lower():
                    email = request.POST.get('email')
                    if Message.objects.filter(email=email).count() >= 3:
                        messages.error(
                            request, "You can't send more than 3 messages!")
                        return redirect('contact')
                    form.save()
                    messages.error(request, "Message has been sent!")
                    return redirect('contact')
                else:
                    messages.error(
                        request, "Email is incorrect or doesn't exist!")
                    return redirect('contact')
            else:
                messages.error(request, "Full name is incorrect!")
                return redirect('contact')

    return render(request, 'projects/include/contact.html', {'form': form, 'check_main': True})
