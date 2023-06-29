
from django.shortcuts import render
from django.http import HttpResponse
from . models import Places
from . models import Team

def demo(request):
    obj = Places.objects.all()
    ob = Team.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})


