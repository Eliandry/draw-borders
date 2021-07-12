from django.shortcuts import render
from .models import Level
from django.views.generic import ListView, DetailView, View


class MainView(ListView):
    model = Level

class LevelDetail(DetailView):
    model=Level



def result(request,pk):
    draw=request.POST.get('imageView')
    lvl=Level.objects.get(id=pk)
    clean=lvl.img
    return render(request,'geoApp/result.html',{'draw':draw,'clean':clean})

