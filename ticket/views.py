from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Ticket


# Create your views here.
class CreateTicekt(CreateView):
    model =Ticket
    fields = ['ticket_title', 'ticket_description']
    template_name = 'ticket/create_ticket.html'
    success_url = '/ticket/view/'