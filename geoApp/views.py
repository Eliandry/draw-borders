from django.shortcuts import render
from .models import Level
from django.views.generic import ListView, DetailView, View


class MainView(ListView):
    model = Level


