from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Project, Category
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
            else:
                messages.error(request, "Full name is incorrect!")
    return render(request, 'projects/index.html', context={'project_list': Project.objects.filter(draft=False), 'category_list': Category.objects.all, 'form': form})


def about(request):
    return render(request, 'include/about.html', {'check_main': True})


def resume(request):
    return render(request, 'include/resume.html', {'check_main': True})


def services(request):
    return render(request, 'include/services.html', {'check_main': True})


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
            else:
                messages.error(request, "Full name is incorrect!")
    return render(request, 'include/contact.html', {'form': form, 'check_main': True})


def category_list(request):
    return render(request, 'projects/category_list.html', context={'category_list': Category.objects.all()})


def project_list(request):
    return render(request, 'projects/project_list.html', context={'category_list': Category.objects.all(), 'project_list': Project.objects.filter(draft=False), 'check_main': True})


def category_detail(request, slug):
    return render(request, 'projects/category_detail.html', context={'category': Category.objects.get(url=slug)})


def project_detail(request, slug, pk):
    try:
        project = Project.objects.get(url=pk)
        if project.draft == False:
            return render(request, 'projects/project_detail.html', context={'project': project})
        else:
            return redirect('project_list')
    except:
        return redirect('project_list')


@login_required(login_url='index')
def message_list(request):
    return render(request, 'projects/message_list.html')
