from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    meetups = [
        {
            'title': 'Meetup_1',
            'location': 'Location_1',
            'slug': 'meetup-1'},
        {
            'title': 'Meetup_2',
            'location': 'Location_2',
            'slug': 'meetup-2'},
    ]

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'Meetup_1',
        'description': 'Description_1',
        'location': 'Location_1',
        'address': 'Address_1',
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
        'meetup_location': selected_meetup['location'],
        'meetup_address': selected_meetup['address'],
    })
