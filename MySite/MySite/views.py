from django.http import Http404


def admin(request):
    raise Http404("You're not allowed here!")
