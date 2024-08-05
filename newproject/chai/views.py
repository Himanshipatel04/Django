from django.shortcuts import render
from . models import ChaiVariety
# Create your views here.
def allchai(request):
    chais = ChaiVariety.objects.all()
    return render(request,"chai/allchai.html",{'chais':chais})