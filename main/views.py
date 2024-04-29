from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Team, About, Services, Portfolio, Clients
from .forms import ContactForm
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.all()
        portfolio = Portfolio.objects.all()
        about = About.objects.all()
        team = Team.objects.all()
        clients = Clients.objects.all()
        form = ContactForm()

        context['services'] = services
        context['portfolio'] = portfolio
        context['about'] = about
        context['team'] = team
        context['clients'] = clients
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('main:index')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)