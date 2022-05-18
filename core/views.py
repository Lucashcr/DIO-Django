from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from core.models import Event


# Create your views here.
def events(request, user):
    user = User.objects.get(username=user)
    events = Event.objects.filter(user=user.id)

    response = f"<h1>Events for user {user.username}</h1>\n"
    for event in events:
        response += "<br>\n"
        response += f"<h2>{event.title}</h2>\n"
        response += f"<p>{event.description}</p>\n"
        response += f"<p>{event.event_date.strftime('%d/%m/%Y %H:%M:%S')}</p>\n"
        
    return HttpResponse(response)