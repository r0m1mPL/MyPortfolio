from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    form = MessageForm
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            if len(request.POST.get('name').split()) in [2, 3]:
                if request.POST.get('email').lower():
                    form = form.save(commit=False)
                    form.email = form.email.lower()
                    form.save()
                    messages.error(request, "Message has been sent!")
                    return redirect('/index/#contact')
                else:
                    messages.error(
                        request, "Email is incorrect or doesn't exist!")
                    return redirect('/index/#contact')
            else:
                messages.error(request, "Full name is incorrect!")
                return redirect('/index/#contact')
    return render(request, 'projects/index.html', context={'form': form})


def about(request):
    return render(request, 'include/about.html', {'check_main': True})


def resume(request):
    return render(request, 'include/resume.html', {'check_main': True})


def contact(request):
    form = MessageForm
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            if len(request.POST.get('name').split()) in [2, 3]:
                if request.POST.get('email').lower():
                    form = form.save(commit=False)
                    form.email = form.email.lower()
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
    return render(request, 'include/contact.html', {'form': form, 'check_main': True})
