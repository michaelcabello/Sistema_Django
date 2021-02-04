from django.shortcuts import render, redirect

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'

    login_url = '/login/'
