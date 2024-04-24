from django.shortcuts import render
from .models import Team, About, Services, Portfolio, Clients


# Create your views here.
def index(request):
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    clients = Clients.objects.all()

    context = {
        'services': services,
        'portfolio': portfolio,
        'about': about,
        'team': team,
        'clients': clients
    }

    return render(request, 'main.html', context)