from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    meetups = [
        {'title': 'Meetup_1'},
        {'title': 'Meetup_2'},
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
