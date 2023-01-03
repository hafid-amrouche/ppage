from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from contact_us.models import Message


def home(request):
    if request.method=="POST":
        email = request.POST.get('email').strip()
        text = request.POST.get('text').strip()
        if email and text :
            Message.objects.create(
                email = email,
                text = text
            )
        else:
            raise
        return HttpResponse()

    title = gettext('Welcome')
    description = gettext('')
    data = {
        'title' : title,
        'description' : description
    }
    return render(request, 'home.html', data)